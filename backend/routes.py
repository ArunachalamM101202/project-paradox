from fastapi import APIRouter
from pydantic import BaseModel
from agent_controller import get_agent_state
from typing import Dict

from dialogue_manager import start_dialogue, add_dialogue_line, end_dialogue
from llm_core import generate_summary
from agent_controller import get_agent_state

from planner import generate_plan, react_override
from agent_controller import get_agent_state

from reflection_engine import reflect
from memory_index import MemoryIndex
from agent_controller import get_agent_state
from fastapi import Query

from belief_emotion_engine import adjust_belief_and_emotion

router = APIRouter()

class ObservationInput(BaseModel):
    text: str
    importance: int = 5
    linked_agent: str = None

class BeliefUpdate(BaseModel):
    target_agent: str
    delta: float

class EmotionUpdate(BaseModel):
    updates: Dict[str, float]

class DialogueLine(BaseModel):
    speaker: str
    listener: str
    text: str

@router.get("/agent/{name}/state")
def get_state(name: str):
    agent = get_agent_state(name)
    return agent.dict()

@router.post("/agent/{name}/observe")
def log_observation(name: str, obs: ObservationInput):
    agent = get_agent_state(name)
    agent.log_observation(obs.text, obs.importance, obs.linked_agent)

    adjust_belief_and_emotion(agent, agent.memory[-1])

    return {"status": "ok", "memory_count": len(agent.memory)}

@router.post("/agent/{name}/belief")
def update_belief(name: str, upd: BeliefUpdate):
    agent = get_agent_state(name)
    agent.update_belief(upd.target_agent, upd.delta)
    return {"new_score": agent.belief_scores[upd.target_agent]}

@router.post("/agent/{name}/emotion")
def update_emotion(name: str, em: EmotionUpdate):
    agent = get_agent_state(name)
    agent.update_emotion(em.updates)
    return {"emotion": agent.emotion_vector}

@router.post("/dialogue/start")
def dialogue_start(a1: str, a2: str):
    start_dialogue(a1, a2)
    return {"status": "started"}

@router.post("/dialogue/speak")
def dialogue_line(d: DialogueLine):
    add_dialogue_line(d.speaker, d.listener, d.text)
    return {"status": "ok"}

@router.post("/dialogue/end")
def dialogue_end(a1: str, a2: str):
    transcript = end_dialogue(a1, a2)
    # Summarize from both perspectives
    for agent, partner in [(a1, a2), (a2, a1)]:
        summary = generate_summary(agent, partner, transcript)
        agent_obj = get_agent_state(agent)
        agent_obj.log_observation(f"Conversation with {partner}: {summary}", importance=6, linked_agent=partner)
    return {"status": "ended", "lines": transcript}

@router.post("/agent/{name}/plan")
def make_plan(name: str):
    agent = get_agent_state(name)
    plan = generate_plan(agent)
    agent.plan = plan
    return {"plan": plan}

@router.post("/agent/{name}/react")
def react_plan(name: str):
    agent = get_agent_state(name)
    new_plan = react_override(agent)
    if new_plan != "KEEP CURRENT PLAN":
        agent.plan = new_plan
    return {"plan": agent.plan}



@router.post("/agent/{name}/reflect")
def run_reflection(name: str):
    return reflect(name)

@router.get("/agent/{name}/retrieve")
def retrieve_memories(name: str, q: str = Query(...)):
    agent = get_agent_state(name)
    index = MemoryIndex()
    index.add_memories(agent.memory)
    results = index.search(q)
    return [{"text": m.text, "score": s} for m, s in results]

@router.post("/agent/{name}/update-belief-emotion")
def update_belief_emotion(name: str):
    agent = get_agent_state(name)
    for mem in agent.memory[-5:]:  # process last 5
        adjust_belief_and_emotion(agent, mem)
    return {
        "belief_scores": agent.belief_scores,
        "emotion_vector": agent.emotion_vector
    }

@router.post("/scenario/test1")
def run_test_scenario():
    # 1. Anna sneaks near the vault
    get_agent_state("Anna").log_observation(
        "Anna went near the vault quietly.", importance=6
    )

    # 2. Arun observes Anna
    get_agent_state("Arun").log_observation(
        "Arun saw Anna sneaking near the vault.", importance=6, linked_agent="Anna"
    )

    # 3. Arun tells John
    get_agent_state("John").log_observation(
        "Arun told me that Anna was sneaking near the vault.", importance=7, linked_agent="Anna"
    )

    # 4. Anna lies to John
    get_agent_state("Anna").log_observation(
        "John asked if I was near the vault. I said no, even though I was.", importance=8, linked_agent="John"
    )

    # 5. John observes the contradiction
    get_agent_state("John").log_observation(
        "Anna told me she was never near the vault. That contradicts what Arun said.", importance=9, linked_agent="Anna"
    )

    return {"status": "Scenario injected"}
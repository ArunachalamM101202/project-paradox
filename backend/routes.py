from fastapi import APIRouter
from pydantic import BaseModel
from agent_controller import get_agent_state
from typing import Dict

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

@router.get("/agent/{name}/state")
def get_state(name: str):
    agent = get_agent_state(name)
    return agent.dict()

@router.post("/agent/{name}/observe")
def log_observation(name: str, obs: ObservationInput):
    agent = get_agent_state(name)
    agent.log_observation(obs.text, obs.importance, obs.linked_agent)
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
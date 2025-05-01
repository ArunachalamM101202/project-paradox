from llm_core import generate_reflection
from agent_controller import get_agent_state
from memory_index import MemoryIndex

REFLECTION_IMPORTANCE_THRESHOLD = 15

def reflect(name: str):
    agent = get_agent_state(name)
    recent = agent.memory[-10:]
    total_importance = sum(m.importance for m in recent)
    if total_importance < REFLECTION_IMPORTANCE_THRESHOLD:
        return {"status": "threshold not met"}

    insights = generate_reflection(name, recent)
    for insight in insights:
        agent.log_observation(f"Reflection: {insight}", importance=6)
    return {"reflections": insights}
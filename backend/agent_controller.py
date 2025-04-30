from models.agent_state import AgentState

# Global dictionary of all agent states
agent_states = {
    name: AgentState(name=name)
    for name in ["John", "Anna", "Arun"]
}

def get_agent_state(name: str) -> AgentState:
    return agent_states.get(name)
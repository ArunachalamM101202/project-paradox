from models.agent_state import AgentState
from memory_index import LongTermMemoryStore

# Global dictionary of all agent states
agent_states = {
    name: AgentState(name=name)
    for name in ["John", "Anna", "Arun"]
}

# Global dictionary of each agent's long-term memory index
long_term_memory = {
    name: LongTermMemoryStore()
    for name in ["John", "Anna", "Arun"]
}

def get_agent_state(name: str) -> AgentState:
    return agent_states.get(name)

def get_long_term_store(name: str) -> LongTermMemoryStore:
    return long_term_memory.get(name)
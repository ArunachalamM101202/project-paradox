from models.agent import Agent

# Sample in-memory agent registry
agents = {
    "John": Agent(name="John", x=2, y=2, status="idle"),
    "Anna": Agent(name="Anna", x=5, y=5, status="idle"),
    "Arun": Agent(name="Arun", x=8, y=2, status="idle")
}

def get_agent(name: str):
    return agents.get(name)

def update_agent(name: str, x: int = None, y: int = None, status: str = None):
    agent = agents.get(name)
    if not agent:
        return None
    if x is not None:
        agent.x = x
    if y is not None:
        agent.y = y
    if status:
        agent.status = status
    return agent
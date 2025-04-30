from pydantic import BaseModel

class Agent(BaseModel):
    name: str
    x: int
    y: int
    status: str
from pydantic import BaseModel

class Command(BaseModel):
    agent: str
    action: str
    target: str = None
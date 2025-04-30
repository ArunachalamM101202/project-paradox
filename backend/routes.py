from fastapi import APIRouter
from models.command import Command
from agent_controller import update_agent

router = APIRouter()

@router.post("/command")
def receive_command(cmd: Command):
    print(f"Received command: {cmd}")
    # Simple logic: walk means status update only
    if cmd.action == "walk":
        update_agent(cmd.agent, status=f"walking to {cmd.target}")
    return {"status": "received"}
from backend.app import socketio
from backend.shared_state import agents

@socketio.on('move_command')
def handle_move(data):
    agent = data['agent']
    new_pos = data['pos']
    agents[agent]['pos'] = new_pos
    agents[agent]['status'] = f"moving to {new_pos}"
    socketio.emit('agent_update', {agent: agents[agent]})
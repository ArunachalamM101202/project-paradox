import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server.")

@sio.event
def disconnect():
    print("Disconnected from server.")

def send_position(agent_name, x, y):
    sio.emit("agent_position", {"agent": agent_name, "x": x, "y": y})
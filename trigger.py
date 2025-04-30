import socketio

sio = socketio.Client()
sio.connect('http://localhost:5000')

# Send move command
sio.emit('move_command', {
    "agent": "John",
    "pos": [4, 2]  # Example target position
})

print("[✓] Move command sent: John -> (4, 2)")
sio.disconnect()
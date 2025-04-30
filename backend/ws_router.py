# web socket handlers

import socketio

sio = socketio.AsyncServer(async_mode='asgi')
socket_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print(f"WebSocket connected: {sid}")

@sio.event
async def agent_position(sid, data):
    print(f"Position from game: {data}")
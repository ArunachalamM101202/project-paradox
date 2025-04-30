# PATCH EARLY!
import eventlet
eventlet.monkey_patch()

from flask import Flask, jsonify
from flask_socketio import SocketIO
from backend.shared_state import agents

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

@app.route('/agents')
def get_agents():
    return jsonify(agents)

# MUST be imported to register WebSocket events
import backend.socket_server

if __name__ == '__main__':
    print("[✓] Backend started with WebSocket support")
    socketio.run(app, host='127.0.0.1', port=5000)
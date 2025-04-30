### **Phase 1: Core Framework Setup**

**Goal**: Pygame + Flask + WebSocket base environment

1. ✅ Create Pygame window with fixed-size map (3 zones: garden, hall, vault)
2. ✅ Place 3 named NPCs with avatars
3. ✅ Set up Flask REST server and Flask-SocketIO for bidirectional comm
4. ✅ Pygame sends:
    - Agent positions
    - Tick updates
5. ✅ Server sends:
    - Actions to perform
    - Dialogues to display
6. ✅ Test:
    - Move NPC from A to B
    - Print JSON response in console
    - Trigger dummy dialogue
7. ✅ Log output: All actions + dialogues


### WORKING ON PHASE 1
	1.	Set up a modular FastAPI backend with REST + WebSocket support.
	2.	Pygame visualizes 3 fixed-position NPCs on a grid.
	3.	Agents move when server sends a command (walk to X).
	4.	Pygame emits real-time position updates over WebSocket.
	5.	All components (backend, state, comms) are cleanly decoupled for future scaling.


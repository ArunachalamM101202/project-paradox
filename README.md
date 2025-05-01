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


🎯 PHASE 2 GOAL

Give each agent a modular internal brain that includes:

	•	✅ A memory stream (observations, dialogues, reflections)
	•	✅ A belief table (trust scores for other agents)
	•	✅ An emotion vector (quantified feelings toward events)

We’ll also:
	•	Expose this via REST APIs (e.g., GET /agent/John/state)
	•	Send dummy observations to test belief/emotion/memory updates
	•	Lay the foundation for reflection + planning in future phases



🧠 PHASE 3: Dialogue + Event Logging + Summary

⸻

🎯 Goal
	•	Enable agents to talk via LLM-generated dialogue.
	•	Log all dialogue lines + create a named transcript file (e.g., dialog_john_anna).
	•	After conversation ends, each agent generates a personal summary of the interaction.
	•	Store that summary in their observation memory using log_observation.

📦 WHAT WE’LL BUILD

✅ Dialogue Manager (dialogue_manager.py)
	•	Stores ongoing dialogue
	•	Logs every line with timestamp
	•	Ends dialogue, returns full history

✅ New REST endpoints
	•	POST /dialogue/start
	•	POST /dialogue/speak
	•	POST /dialogue/end

✅ Summary generation using Ollama (LLM)
	•	Prompt LLM to summarize a dialogue from one agent’s perspective
	•	Add to their memory as MemoryItem

PHASE 3 Summary:
✅ Memory Structure Breakdown:
	•	Agent: John
	•	Memory: Includes a personalized LLM summary of the dialogue
	•	Belief scores: Empty for now (we’ll use this in Phase 4)
	•	Emotion vector: Untouched so far (also Phase 4+)


PHASE 4 SUMMARY

✅ What We’ll Build
	1.	🔧 Add plan field to AgentState
	2.	✍️ Create LLM-powered daily planner
	3.	🔄 Add reaction override logic (based on memory/emotion/belief)
	4.	🌐 REST APIs to:
	•	Get current plan
	•	Generate a new plan
	•	React to an observation
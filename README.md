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


PHASE 5 GOAL

Give each agent the ability to reflect periodically on their past events and generate high-level insights, and to retrieve relevant memories using a Recency, Relevance, and Importance (BERRI) weighted scoring system.

⸻

✅ What We’ll Do
	1.	Add FAISS to index agent memory embeddings.
	2.	Create a RAG (Retrieval-Augmented Generation) system to fetch top-K relevant memories using cosine similarity.
	3.	Implement Reflection Trigger Logic:
	•	If recent memories cross importance threshold, summarize them via LLM.
	4.	Add REST endpoints:
	•	GET /agent/{name}/retrieve?q=...
	•	POST /agent/{name}/reflect



Phase 6 — Scripted Scenario + Deduction Loop

This is where you bring all systems together for a full simulation cycle:

You’ll finally see:
	•	🧠 Agents make a plan
	•	🗣️ Talk and remember
	•	🤨 Reflect on what happened
	•	🤯 React if things seem off
	•	🧾 Build suspicion through memory

✅ What We’ll Build
	1.	Add an API: POST /scenario/test1
→ Inject 3–4 scripted memories (some true, some false)
	2.	Let agents talk using dialogue API
	3.	Trigger /reflect + /react to see deduction happen
	4.	Final: use /state to see if belief/emotion updated

🧠 Phase 7: Belief Scoring + Emotion Feedback Loop

⸻

🎯 GOAL

Create a modular, score-based system that lets agents:

	•	Adjust belief (trust) in other agents
	•	Adjust emotions like suspicion, stress, anger
	•	Trigger these updates from memory events and dialogue

⸻

✅ What We’ll Build

🔸 1. Emotion + Belief Hooks

When a memory is logged (via /observe or /dialogue), we:
	•	Analyze the content
	•	Adjust the agent’s belief_scores
	•	Adjust their emotion_vector

🔸 2. Add REST API:
	•	/agent/{name}/update-belief-emotion

Processes existing memory and updates state

🔸 3. Add LLM hook (optional override)

Ask: “How should John feel about Anna based on this?”

⸻

🧱 Update Strategy (Lightweight & Modular)

To keep things flexible:
	•	All emotion + belief updates go into a single helper file:
belief_emotion_engine.py
	•	This file is auto-called whenever an observe or dialogue_end happens


 Phase 8: Memory Compression + RAG (FAISS) Integration

⸻

🎯 GOAL

Agents store tons of events over time. We now:

	•	Offload old memory into compressed summaries
	•	Store embeddings via FAISS
	•	Retrieve contextually relevant memories for planning, reacting, etc.

This mimics:
	•	💾 Short-term memory → agent.memory (live)
	•	📚 Long-term memory → summarized + vectorized via FAISS
	•	🧠 Use both during LLM prompts for plan, react, reflect


✅ What We’ll Build
	1.	🔁 Move old memory (>N) into summary
	2.	🧠 Run LLM compression: summarize 3–5 logs into 1 compressed item
	3.	💾 Store compressed text + FAISS embedding
	4.	🔍 Add retrieve_memories(query) → RAG from compressed memory
	5.	🔌 Update /plan, /react, /reflect to optionally include top-K relevant past summaries
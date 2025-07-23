# Project Paradox

Project Paradox is a scalable, plug-and-play multi-agent AI framework designed to bring intelligent, emotionally aware, and memory-driven agents to life in any game or interactive simulation. Developed at Supercell’s AI Innovation Lab, Project Paradox combines cutting-edge LLM orchestration, vector memory subsystems, and modular backend APIs to enable lifelike planning, spatial reasoning, and emergent behavior.

⸻

## Key Features

Agent Intelligence
	•	Modular Cognitive Stack:
	•	Long-term memory with FAISS-based vector store (1M+ embeddings supported)
	•	Agent-specific beliefs, emotions, and personality vectors
	•	Dynamic planning and reflection loop triggered by memory
	•	Conversational AI:
	•	LLM-agnostic architecture: works with GPT, Gemini, LLaMA, Claude, or any open-source model
	•	Agents speak in-character with contextual awareness of the world and their past

⸻

World Awareness
	•	Spatial Context Modeling:
	•	Agents know where they are, who is near them, and what objects are present
	•	Location-aware behavior and dialogue grounded in real-time game state
	•	Dynamic Story Trigger System:
	•	Broadcast in-world events (e.g., parties, disasters, deaths)
	•	Agents update memory, react emotionally, and change plans autonomously
	•	Universal Game Prompt Framework:
	•	Generate entire gameplay scenarios from a single natural language prompt
	•	Example: instantly spin up a murder mystery, cozy sim, or survival game by changing one line

⸻

Backend Architecture
	•	FastAPI microservices powering:
	•	Memory management
	•	LLM response orchestration
	•	World-state sync with game engine (Unity, Unreal, Web, etc.)
	•	FAISS-powered Retrieval System:
	•	High-dimensional similarity search for memory recall
	•	Embedding compression + agent-specific storage
	•	Plug-and-play APIs:
	•	/memory, /plan, /dialogue, /summary, /location, and more
	•	Easy integration with game engines or simulation environments

⸻

Platform Compatibility
	•	✅ Unity, Unreal Engine, Godot
	•	✅ Web, Mobile, VR/AR
	•	✅ Deployable to any cloud platform or run entirely offline on-device
	•	✅ Works with local LLM inference (e.g., Ollama, llama.cpp) or hosted APIs (OpenAI, Gemini, Claude)

⸻

Future Work
	•	Reinforcement Learning for long-term planning
	•	Multi-agent belief propagation and theory of mind modeling
	•	Auto-curated memory pruning and episodic summarization
	•	Integration with physical robots and embodied agents

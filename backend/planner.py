import ollama
from models.agent_state import AgentState

import ollama
from models.agent_state import AgentState

def generate_plan(agent: AgentState, long_term_store) -> str:
    recent_memories = agent.memory[-5:]
    recent_lines = "\n".join([f"- {m.text}" for m in recent_memories])

    rag_memories = long_term_store.retrieve(agent.name, k=3)
    rag_lines = "\n".join([f"- {m.text}" for m in rag_memories])

    prompt = f"""
You are {agent.name}, an NPC in a social deduction game.

Recent Observations:
{recent_lines}

Important Past Experiences:
{rag_lines}

Based on this, generate one concise sentence describing {agent.name}'s next immediate plan.
Format: <Agent> plans to <do something>.
No explanation.
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()


def react_override(agent: AgentState, long_term_store) -> str:
    recent_memories = agent.memory[-3:]
    recent_lines = "\n".join([f"- {m.text}" for m in recent_memories])

    rag_memories = long_term_store.retrieve(agent.name, k=3)
    rag_lines = "\n".join([f"- {m.text}" for m in rag_memories])

    prompt = f"""
You are {agent.name}, an NPC in a social deduction game.

Current plan: {agent.plan}

Recent Observations:
{recent_lines}

Important Past Experiences:
{rag_lines}

Should your plan change? If not, reply exactly: KEEP CURRENT PLAN.
If yes, reply with: NEW PLAN: <one sentence action, no explanation>.
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()
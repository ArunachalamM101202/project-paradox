import ollama
from models.agent_state import AgentState

def generate_plan(agent: AgentState) -> str:
    prompt = f"""
You are {agent.name}, an NPC in a social deduction game.

Current emotional state: {agent.emotion_vector}
Recent memories:
{chr(10).join([f"- {m.text}" for m in agent.memory[-5:]])}

Based on the above, generate ONE concise sentence describing {agent.name}'s next immediate plan. Keep it short and in-character.

Format: <Agent> plans to <do something>. Do not include explanations or lists.
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()

def react_override(agent: AgentState) -> str:
    print(f"Current plan: {agent.plan}\n\n")
    prompt = f"""
You are {agent.name}, an NPC in a social deduction game.

Your current plan is: {agent.plan}

Recent emotional state:
{agent.emotion_vector}

Your last 3 observations:
{chr(10).join([f"- {m.text}" for m in agent.memory[-3:]])}

Decide if the current plan still makes sense given the new information. If it's already covering the situation, reply exactly: KEEP CURRENT PLAN.

If there's new information (e.g., contradictions, deception, threats) that require a different response, return a NEW PLAN in this format:

NEW PLAN: <one sentence action, concise and in-character.>

DO NOT explain anything — just return the directive.
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response['message']['content'])  # for debugging only
    print("\n\n")
    return response['message']['content'].strip()
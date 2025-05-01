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
    prompt = f"""
You are {agent.name}, an NPC in a social deduction game.

Current plan: {agent.plan}
Recent emotional state: {agent.emotion_vector}
Recent memories:
{chr(10).join([f"- {m.text}" for m in agent.memory[-3:]])}

Check if the agent's plan should change. If nothing is suspicious, or similar to current plan then respond exactly: KEEP CURRENT PLAN

If something recently happened that might cause suspicion or change in behavior, return a NEW plan in this format:

NEW PLAN: <one sentence action, concise and in-character>.

Avoid explanation or context. Just the directive.
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()
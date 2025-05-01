import ollama

def generate_summary(agent: str, partner: str, dialogue: list[str]) -> str:
    joined = "\n".join(dialogue)
    prompt = f"""
You are {agent}. Summarize this conversation from your point of view.

Conversation with {partner}:
{joined}

Summary (1-2 sentences):"""

    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content'].strip()

def generate_reflection(agent_name: str, memories: list):
    formatted = "\n".join([f"{i+1}. {m.text}" for i, m in enumerate(memories)])
    prompt = f"""
You are {agent_name}, an NPC in a social deduction game.

Here are your recent observations:
{formatted}

Reflect on these events and summarize three key high-level insights as a single paragraph. Be concise, stay in-character, and do not list bullet points or preamble. Just write the reflection as one flowing paragraph.
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return [f"Reflection: {response['message']['content'].strip()}"]


def summarize_memories(agent_name: str, memories: list):
    text = "\n".join([f"- {m.text}" for m in memories])
    prompt = f"""
You are {agent_name}. The following are multiple short memories.

{text}

Summarize these into one concise memory entry in paragraph form. Be abstract and high-level, but accurate.
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()
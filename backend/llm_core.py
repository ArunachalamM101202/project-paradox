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
You are {agent_name}. Here are your recent observations:

{formatted}

What are 3 high-level insights or thoughts you have based on these observations? Format like:
- <insight>
- <insight>
- <insight>
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    lines = response['message']['content'].split("\n")
    return [line.strip("- ").strip() for line in lines if line.strip()]
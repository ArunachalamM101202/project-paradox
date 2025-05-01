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
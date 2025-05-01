from llm_core import summarize_memories
from models.agent_state import MemoryItem
from datetime import datetime
import hashlib

def memory_block_hash(mem_block: list) -> str:
    joined = "|".join(m.text for m in mem_block)
    return hashlib.md5(joined.encode()).hexdigest()

def compress_memory(agent, long_term_store):
    if len(agent.memory) < 5:
        return None

    to_compress = agent.memory[:5]
    hash_id = memory_block_hash(to_compress)

    if hash_id in agent.compressed_ids:
        return None  # Already compressed this batch

    summary = summarize_memories(agent.name, to_compress)
    summary_item = MemoryItem(
        text=f"Compressed: {summary}",
        timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        importance=6
    )

    agent.memory = agent.memory[5:]
    agent.compressed_ids.add(hash_id)
    long_term_store.add_summary(summary_item)
    return summary_item
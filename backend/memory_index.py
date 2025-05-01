import faiss
from sentence_transformers import SentenceTransformer
from models.agent_state import MemoryItem

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

class MemoryIndex:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)
        self.memories = []
        self.texts = []

    def add_memories(self, memory_list: list[MemoryItem]):
        self.memories = memory_list
        self.texts = [m.text for m in memory_list]
        embeddings = embedding_model.encode(self.texts)
        self.index.reset()
        self.index.add(embeddings)

    def search(self, query: str, k=5):
        q_vec = embedding_model.encode([query])
        scores, indices = self.index.search(q_vec, k)
        return [(self.memories[i], float(scores[0][idx])) for idx, i in enumerate(indices[0]) if i < len(self.memories)]
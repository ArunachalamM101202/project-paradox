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
    
class LongTermMemoryStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)
        self.embeddings = []
        self.items = []
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def add_summary(self, item: MemoryItem):
        existing_texts = [m.text.strip() for m in self.embeddings]
        if item.text.strip() in existing_texts:
            return  # Skip exact dupes
        emb = self.model.encode([item.text])
        self.embeddings.append(item)
        self.index.add(emb)

    def retrieve(self, query: str, k=3):
        q_vec = self.model.encode([query])
        scores, indices = self.index.search(q_vec, k)
        
        seen = set()
        results = []

        for i in indices[0]:
            if i >= len(self.embeddings):
                continue
            text = self.embeddings[i].text.strip()
            if text in seen:
                continue
            seen.add(text)
            results.append(self.embeddings[i])

        return results
from .embedding_model import embed_text
import numpy as np

def load_embeddings(path="data_embeddings.npz"):
    data = np.load(path, allow_pickle=True)
    return data["embeddings"], data["filenames"], data["texts"]

def semantic_search(query, embeddings, filenames, texts, top_k=5):
    query_emb = embed_text(query)
    similarities = np.dot(embeddings, query_emb) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb) + 1e-8
    )
    top_indices = np.argsort(similarities)[::-1][:top_k]
    results = []
    for idx in top_indices:
        results.append({
            "filename": filenames[idx],
            "text": texts[idx],
            "score": float(similarities[idx])
        })
    return results
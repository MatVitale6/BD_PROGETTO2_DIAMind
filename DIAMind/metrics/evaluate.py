import os
import csv

# importa search e ground_truth
from DIAMind.search import load_embeddings, semantic_search
try:
    from DIAMind.metrics.ground_truth import ground_truth
except Exception:
    from .ground_truth import ground_truth

def reciprocal_rank(results, correct_filename):
    """
    Cerca il documento corretto nella lista results (ordine decrescente di rilevanza).
    Restituisce 1/(rank) oppure 0.0 se non trovato.
    """
    for i, r in enumerate(results):
        fname = r.get("filename", "")
        # confronto permissivo: esatto o substring
        if fname == correct_filename or correct_filename in fname or fname in correct_filename:
            return 1.0 / (i + 1)
    return 0.0

def evaluate(top_k=10, embeddings_path=None, out_csv="metrics_ranking.csv"):
    # trova data_embeddings.npz nella cartella DIAMind
    if embeddings_path is None:
        embeddings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_embeddings.npz")
    embeddings, filenames, texts = load_embeddings(embeddings_path)

    scores = []
    rows = []
    for query, correct in ground_truth.items():
        results = semantic_search(query, embeddings, filenames, texts, top_k=top_k)
        rr = reciprocal_rank(results, correct)
        rank = int(1/rr) if rr > 0 else None
        scores.append(rr)
        rows.append({
            "query": query,
            "correct": correct,
            "rr": rr,
            "rank": rank
        })
        print(f"Query: {query!r}  RR={rr:.4f}  rank={rank}")

    mrr = sum(scores) / len(scores) if scores else 0.0
    print(f"\nMRR@{top_k} = {mrr:.4f}  (calcolato su {len(scores)} query)")

    # salva CSV con dettagli
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["query", "correct", "rr", "rank"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Dettagli salvati in: {out_csv}")

if __name__ == "__main__":
    evaluate(top_k=10)
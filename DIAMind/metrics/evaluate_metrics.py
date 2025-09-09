import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

# assicurati che la root del progetto sia nel path per importare il package DIAMind
proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from DIAMind.search import load_embeddings, semantic_search

# carica ground truth: prova il modulo Python, altrimenti legge il CSV ground_truth_labelled.csv
try:
    from DIAMind.metrics.ground_truth import ground_truth
except Exception:
    ground_truth = {}
    gt_csv_path = os.path.join(os.path.dirname(__file__), "ground_truth_labelled.csv")
    if os.path.exists(gt_csv_path):
        with open(gt_csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = row.get("query", "").strip()
                corr = row.get("correct", "").strip()
                if not q:
                    continue
                if not corr:
                    # mantieni voce ma vuota (opzionale: puoi saltare)
                    ground_truth[q] = ""
                    continue
                # supporta più file separati da ';'
                if ";" in corr:
                    ground_truth[q] = [s.strip() for s in corr.split(";") if s.strip()]
                else:
                    ground_truth[q] = corr
    else:
        print(f"Warning: ground truth module non trovato e file CSV mancante: {gt_csv_path}")

def normalize_gt_entry(v):
    if v is None or v == "" or (isinstance(v, list) and len(v) == 0):
        return []
    if isinstance(v, str):
        # supporta più file separati da ';' eventualmente
        if ";" in v:
            return [s.strip() for s in v.split(";") if s.strip()]
        return [v]
    if isinstance(v, (list, tuple, set)):
        return list(v)
    return [str(v)]

def reciprocal_rank(results, correct_set):
    for i, r in enumerate(results):
        fname = r.get("filename", "")
        for c in correct_set:
            if fname == c or c in fname or fname in c:
                return 1.0 / (i + 1), i + 1
    return 0.0, None

def evaluate(embeddings_path=None, eval_k=50, out_csv="metrics_detailed.csv", plots_dir="metrics_plots"):
    if embeddings_path is None:
        embeddings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_embeddings.npz")
    embeddings, filenames, texts = load_embeddings(embeddings_path)

    ks = list(range(1, min(eval_k, 50) + 1))  # ks for precision/hit curves
    sum_rr = 0.0
    rr_list = []
    ranks = []
    per_query_rows = []

    # accumulators for precision/hit
    precisions_at_k = np.zeros(len(ks), dtype=float)
    hits_at_k = np.zeros(len(ks), dtype=float)
    n_queries = 0

    for query, gt_val in ground_truth.items():
        correct = normalize_gt_entry(gt_val)
        if not correct:
            # skip queries without a labeled correct document
            continue
        n_queries += 1
        results = semantic_search(query, embeddings, filenames, texts, top_k=eval_k)
        rr, rank = reciprocal_rank(results, correct)
        sum_rr += rr
        rr_list.append(rr)
        ranks.append(rank if rank is not None else 0)
        per_query_rows.append({
            "query": query,
            "correct": ";".join(correct),
            "rr": rr,
            "rank": rank if rank is not None else ""
        })

        # compute precision@k and hit@k for this query (single/multiple correct supported)
        for idx, k in enumerate(ks):
            topk = results[:k]
            found = 0
            for r in topk:
                for c in correct:
                    if r["filename"] == c or c in r["filename"] or r["filename"] in c:
                        found += 1
                        break
            precisions_at_k[idx] += (found / k)
            hits_at_k[idx] += (1.0 if found > 0 else 0.0)

    if n_queries == 0:
        print("Nessuna query valida trovata nella ground truth. Controlla ground_truth.py")
        return

    mrr = sum_rr / n_queries
    mean_prec_at_k = precisions_at_k / n_queries
    hit_rate_at_k = hits_at_k / n_queries

    os.makedirs(plots_dir, exist_ok=True)

    # Plot Precision@k
    plt.figure(figsize=(8,4))
    plt.plot(ks, mean_prec_at_k, marker='o')
    plt.xlabel("k")
    plt.ylabel("Precision@k (media)")
    plt.title(f"Precision@k (n={n_queries})")
    plt.grid(True)
    prec_plot = os.path.join(plots_dir, "precision_at_k.png")
    plt.savefig(prec_plot, bbox_inches='tight', dpi=150)
    plt.close()

    # Plot HitRate@k
    plt.figure(figsize=(8,4))
    plt.plot(ks, hit_rate_at_k, marker='o', color='tab:orange')
    plt.xlabel("k")
    plt.ylabel("HitRate@k (fraction of queries with at least one relevant in top-k)")
    plt.title(f"HitRate@k (n={n_queries})")
    plt.grid(True)
    hit_plot = os.path.join(plots_dir, "hitrate_at_k.png")
    plt.savefig(hit_plot, bbox_inches='tight', dpi=150)
    plt.close()

    # Histogram of ranks (only found queries)
    found_ranks = [r for r in ranks if r and r > 0]
    if found_ranks:
        plt.figure(figsize=(8,4))
        plt.hist(found_ranks, bins=range(1, max(found_ranks)+2), align='left', color='tab:green')
        plt.xlabel("Rank (1 = primo risultato)")
        plt.ylabel("Numero di query")
        plt.title("Distribuzione dei rank per query trovate")
        plt.grid(axis='y')
        rank_plot = os.path.join(plots_dir, "ranks_histogram.png")
        plt.savefig(rank_plot, bbox_inches='tight', dpi=150)
        plt.close()
    else:
        rank_plot = None

    # save detailed CSV
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["query", "correct", "rr", "rank"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(per_query_rows)

    # print summary
    print(f"Queries valutate: {n_queries}")
    print(f"MRR@{eval_k}: {mrr:.4f}")
    for k in [1,3,5,10]:
        if k <= len(ks):
            print(f"Precision@{k}: {mean_prec_at_k[k-1]:.4f}   HitRate@{k}: {hit_rate_at_k[k-1]:.4f}")
    print(f"Grafici salvati in: {plots_dir}")
    if rank_plot:
        print(f"Istogramma rank salvato in: {rank_plot}")
    print(f"Dettagli per query salvati in: {out_csv}")

if __name__ == "__main__":
    evaluate(embeddings_path=None, eval_k=50, out_csv="metrics_detailed.csv", plots_dir="DIAMind/metrics/plots")

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
                    ground_truth[q] = ""
                    continue
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

    # plot_ks: usa fino a 50 o eval_k se minore (rimesso a 50 come richiesto)
    max_plot_k = min(eval_k, 50)
    plot_ks = list(range(1, max_plot_k + 1))

    sum_rr = 0.0
    rr_list = []
    ranks = []
    per_query_rows = []

    # accumulators per precision/hit sui plot_ks
    precisions_at_k = np.zeros(len(plot_ks), dtype=float)
    hits_at_k = np.zeros(len(plot_ks), dtype=float)
    n_queries = 0

    for query, gt_val in ground_truth.items():
        correct = normalize_gt_entry(gt_val)
        if not correct:
            continue
        n_queries += 1
        # la ricerca prende top eval_k; i plot user vogliono considerare solo k<=3
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

        # compute precision@k and hit@k for plot_ks
        for idx, k in enumerate(plot_ks):
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

    # Plot Precision@k (ora k fino a max_plot_k, default 50)
    plt.figure(figsize=(8,3))
    plt.plot(plot_ks, mean_prec_at_k, marker='o', markersize=4, linewidth=1)
    # ticks leggibili: mostra tutti se pochi, altrimenti una selezione
    if len(plot_ks) <= 15:
        plt.xticks(plot_ks)
    else:
        ticks = sorted(set([1,2,3,5,10,20, max_plot_k]))
        plt.xticks([t for t in ticks if t <= max_plot_k])
    plt.xlabel("k")
    plt.ylabel("Precision@k (media)")
    plt.title(f"Precision@k (n={n_queries})")
    plt.grid(True)
    prec_plot = os.path.join(plots_dir, "precision_at_k.png")
    plt.savefig(prec_plot, bbox_inches='tight', dpi=150)
    plt.close()

    # Plot HitRate@k (ora k fino a max_plot_k, default 50)
    plt.figure(figsize=(8,3))
    plt.plot(plot_ks, hit_rate_at_k, marker='o', markersize=4, linewidth=1, color='tab:orange')
    if len(plot_ks) <= 15:
        plt.xticks(plot_ks)
    else:
        ticks = sorted(set([1,2,3,5,10,20, max_plot_k]))
        plt.xticks([t for t in ticks if t <= max_plot_k])
    plt.xlabel("k")
    plt.ylabel("HitRate@k")
    plt.title(f"HitRate@k (n={n_queries})")
    plt.grid(True)
    hit_plot = os.path.join(plots_dir, "hitrate_at_k.png")
    plt.savefig(hit_plot, bbox_inches='tight', dpi=150)
    plt.close()

    # Histogram of ranks limitato a 1..3, barre con colori distinti e tick interi
    found_ranks = [r for r in ranks if r and r > 0 and r <= 3]
    if found_ranks:
        plt.figure(figsize=(6,3))
        bins = [1,2,3]
        counts = [found_ranks.count(b) for b in bins]
        # colori distinti per rank 1,2,3
        colors = ['#4caf50', '#ff9800', '#2196f3']
        # assicurati che la lista colori sia lunga quanto le barre
        bar_colors = [colors[i % len(colors)] for i in range(len(counts))]
        # debug: stampa conteggi prima del plot
        print("Rank counts (1..3):", dict(zip(bins, counts)))
        x_pos = bins
        plt.bar(x_pos, counts, color=bar_colors, align='center', width=0.6, edgecolor='black')
        plt.xticks(bins)
        plt.xlim(0.5, 3.5)
        plt.xlabel("Rank (1 = primo risultato)")
        plt.ylabel("Numero di query")
        plt.title("Distribuzione dei rank (solo 1-3)")
        plt.grid(axis='y')
        rank_plot = os.path.join(plots_dir, "ranks_histogram.png")
        plt.savefig(rank_plot, bbox_inches='tight', dpi=150)
        plt.close()
    else:
        rank_plot = None

    # salva CSV dettagliato
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["query", "correct", "rr", "rank"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(per_query_rows)

    # stampa riepilogo
    print(f"Queries valutate: {n_queries}")
    print(f"MRR@{eval_k}: {mrr:.4f}")
    for k in [1,3]:
        idx = plot_ks.index(k) if k in plot_ks else None
        if idx is not None:
            print(f"Precision@{k}: {mean_prec_at_k[idx]:.4f}   HitRate@{k}: {hit_rate_at_k[idx]:.4f}")
    print(f"Grafici salvati in: {plots_dir}")
    if rank_plot:
        print(f"Istogramma rank salvato in: {rank_plot}")
    print(f"Dettagli per query salvati in: {out_csv}")

if __name__ == "__main__":
    evaluate(embeddings_path=None, eval_k=50, out_csv="metrics_detailed.csv", plots_dir="DIAMind/metrics/plots")

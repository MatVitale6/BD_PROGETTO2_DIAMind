import os
import csv
import textwrap
import sys

# assicurati che la root del progetto (cartella che contiene DIAMind/) sia nel path
proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from DIAMind.search import load_embeddings, semantic_search

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data", "Cleaned")
EMBED_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_embeddings.npz")

def prompt_select(results, snippet_len=300):
    """
    Stampa i risultati e chiede all'utente quali indici sono corretti.
    Restituisce lista di filenames selezionati (può essere vuota).
    """
    for i, r in enumerate(results, start=1):
        snippet = r["text"].strip().replace("\n", " ")
        if len(snippet) > snippet_len:
            snippet = snippet[:snippet_len].rsplit(" ", 1)[0] + "..."
        print(f"[{i}] {r['filename']} (score={r['score']:.4f})")
        print("    " + textwrap.fill(snippet, width=90, subsequent_indent="    "))
    print()
    sel = input("Inserisci indici corretti separati da virgola (o 'n' per nessuno, 'f' per inserire filename manuale): ").strip()
    if not sel:
        return []
    if sel.lower() == 'n':
        return []
    if sel.lower() == 'f':
        fname = input("Inserisci il nome esatto del file corretto: ").strip()
        return [fname] if fname else []
    # parse comma-separated indices
    chosen = []
    for token in sel.split(","):
        token = token.strip()
        if not token:
            continue
        try:
            idx = int(token)
            if 1 <= idx <= len(results):
                chosen.append(results[idx-1]["filename"])
        except ValueError:
            # treat token as filename
            chosen.append(token)
    return chosen

def build_from_queries(queries, top_k=10, out_csv="ground_truth_labelled.csv"):
    embeddings, filenames, texts = load_embeddings(EMBED_PATH)
    rows = []
    gt = {}
    for q in queries:
        print("\n" + "="*80)
        print("Query:", q)
        results = semantic_search(q, embeddings, filenames, texts, top_k=top_k)
        selected = prompt_select(results)
        if selected:
            gt_val = selected if len(selected) > 1 else selected[0]
            gt[q] = gt_val
            rows.append({"query": q, "correct": ";".join(selected)})
        else:
            rows.append({"query": q, "correct": ""})
        # optional quick save after each step
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["query", "correct"])
            writer.writeheader()
            writer.writerows(rows)
    # write ground_truth.py
    gt_path = os.path.join(os.path.dirname(__file__), "ground_truth.py")
    with open(gt_path, "w", encoding="utf-8") as f:
        f.write("# Auto-generated ground_truth mapping\n")
        f.write("ground_truth = {\n")
        for k, v in gt.items():
            if isinstance(v, list):
                vals = ", ".join(repr(x) for x in v)
                f.write(f"    {repr(k)}: [{vals}],\n")
            else:
                f.write(f"    {repr(k)}: {repr(v)},\n")
        f.write("}\n")
    print(f"\nSalvato CSV: {out_csv}")
    print(f"Salvato ground truth Python: {gt_path}")

def load_queries_from_file(path):
    qs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                qs.append(line)
    return qs

def main():
    print("BUILD GROUND TRUTH INTERATTIVO")
    mode = input("Modalità: (1) inserire queries manualmente, (2) caricare file di queries (una per riga) [1/2]: ").strip() or "1"
    if mode == "2":
        path = input("Percorso file queries: ").strip()
        if not os.path.exists(path):
            print("File non trovato.")
            return
        queries = load_queries_from_file(path)
    else:
        print("Inserisci le query. Digita una riga vuota per terminare.")
        queries = []
        while True:
            q = input("Query: ").strip()
            if q == "":
                break
            queries.append(q)
    if not queries:
        print("Nessuna query fornita. Esco.")
        return
    top_k = input("Top-K da mostrare per ogni query (default 10): ").strip()
    top_k = int(top_k) if top_k.isdigit() else 10
    out_csv = input("Nome CSV di output (default ground_truth_labelled.csv): ").strip() or "ground_truth_labelled.csv"
    build_from_queries(queries, top_k=top_k, out_csv=out_csv)

if __name__ == "__main__":
    main()
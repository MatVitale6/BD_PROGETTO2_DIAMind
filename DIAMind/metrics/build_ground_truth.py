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
GT_CSV = os.path.join(os.path.dirname(__file__), "ground_truth_labelled.csv")
GT_PY = os.path.join(os.path.dirname(__file__), "ground_truth.py")

def load_existing_ground_truth():
    """Carica ground truth da ground_truth.py e/o CSV (unisce, py ha priorità)."""
    gt = {}
    # carica da py se esiste
    if os.path.exists(GT_PY):
        try:
            ns = {}
            with open(GT_PY, "r", encoding="utf-8") as f:
                exec(f.read(), ns)
            if "ground_truth" in ns and isinstance(ns["ground_truth"], dict):
                gt.update(ns["ground_truth"])
        except Exception:
            pass
    # carica da csv e integra (ma non sovrascrive voci già presenti)
    if os.path.exists(GT_CSV):
        try:
            with open(GT_CSV, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    q = row.get("query", "").strip()
                    corr = row.get("correct", "").strip()
                    if not q:
                        continue
                    if q in gt:
                        continue
                    if ";" in corr:
                        gt[q] = [s.strip() for s in corr.split(";") if s.strip()]
                    else:
                        gt[q] = corr
        except Exception:
            pass
    return gt

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
    # carica embeddings
    embeddings, filenames, texts = load_embeddings(EMBED_PATH)
    # carica ground truth esistente
    existing_gt = load_existing_ground_truth()
    rows = []
    new_entries = {}

    for q in queries:
        print("\n" + "="*80)
        print("Query:", q)
        # se già presente chiedi se sovrascrivere
        if q in existing_gt:
            print("Esiste già una voce per questa query nella ground truth.")
            print("Valore attuale:", existing_gt[q])
            choice = input("Vuoi (s)altare, (v)isualizzare risultati per riesaminare, (r)iscrivere/sovrascrivere? [s/v/r]: ").strip().lower() or "s"
            if choice == "s":
                # mantieni esistente
                val = existing_gt[q]
                if isinstance(val, list):
                    rows.append({"query": q, "correct": ";".join(val)})
                else:
                    rows.append({"query": q, "correct": val})
                continue
            elif choice == "v":
                # prosegui ed elabora come nuova etichettatura ma mostra prima i risultati
                pass
            elif choice == "r":
                # procederà a rideterminare la voce
                pass

        results = semantic_search(q, embeddings, filenames, texts, top_k=top_k)
        selected = prompt_select(results)
        if selected:
            gt_val = selected if len(selected) > 1 else selected[0]
            new_entries[q] = gt_val
            rows.append({"query": q, "correct": ";".join(selected)})
        else:
            # salva come vuoto (se non presente prima)
            rows.append({"query": q, "correct": ""})

        # salva CSV parziale ogni iterazione per non perdere lavoro
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["query", "correct"])
            writer.writeheader()
            # unisci existing + new_entries + current rows (ordine: existing keys first)
            merged = dict(existing_gt)
            merged.update(new_entries)
            # aggiorna con rows per garantire ordine di inserimento
            for r in rows:
                merged[r["query"]] = [] if r["correct"] == "" else ([s.strip() for s in r["correct"].split(";")] if ";" in r["correct"] else r["correct"])
            for k, v in merged.items():
                if isinstance(v, list):
                    corr = ";".join(v)
                else:
                    corr = v
                writer.writerow({"query": k, "correct": corr})

    # final merge: existing_gt <- new_entries
    merged_gt = dict(existing_gt)
    merged_gt.update(new_entries)

    # scrivi ground_truth.py aggiornato
    with open(GT_PY, "w", encoding="utf-8") as f:
        f.write("# Auto-generated ground_truth mapping\n")
        f.write("ground_truth = {\n")
        for k in sorted(merged_gt.keys()):
            v = merged_gt[k]
            if isinstance(v, list):
                vals = ", ".join(repr(x) for x in v)
                f.write(f"    {repr(k)}: [{vals}],\n")
            else:
                f.write(f"    {repr(k)}: {repr(v)},\n")
        f.write("}\n")

    # scrivi CSV finale (ordinato)
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["query", "correct"])
        writer.writeheader()
        for k in sorted(merged_gt.keys()):
            v = merged_gt[k]
            if isinstance(v, list):
                corr = ";".join(v)
            else:
                corr = v
            writer.writerow({"query": k, "correct": corr})

    print(f"\nSalvato CSV: {out_csv}")
    print(f"Salvato ground truth Python: {GT_PY}")

def load_queries_from_file(path):
    qs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                qs.append(line)
    return qs

def main():
    print("BUILD GROUND TRUTH INTERATTIVO (AGGIUNTA SENZA PERDERE ESISTENTI)")
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
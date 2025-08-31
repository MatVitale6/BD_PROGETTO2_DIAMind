import os
import numpy as np
from embedding_model import embed_many

DATA_DIR = "/home/matteo/BD_PROGETTO2_DIAMind/BD_PROGETTO2_DIAMind/Data/Cleaned"
texts = []
filenames = []

# Leggi tutti i file .md e .identifier
for fname in os.listdir(DATA_DIR):
    if fname.endswith(".md") or fname.endswith(".identifier"):
        with open(os.path.join(DATA_DIR, fname), "r", encoding="utf-8") as f:
            texts.append(f.read())
            filenames.append(fname)

# Embeddizza tutti i testi
embeddings = embed_many(texts)

# Salva embeddings e nomi file
np.savez("data_embeddings.npz", embeddings=embeddings, filenames=filenames, texts=texts)
print(f"Salvati {len(texts)} embedding in data_embeddings.npz")
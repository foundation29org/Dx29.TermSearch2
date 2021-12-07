import numpy as np

def _load_embeddings(fn):
    return np.load(fn)

a = _load_embeddings('_embs/symptoms-en.npy')
b = _load_embeddings('_output/paraphrase-MiniLM-L6-v2-symptoms-en.npy')

for x, y in zip(a, b):
    for n, m in zip(x, y):
        if abs(n - m) > 1e-5:
            print(abs(n - m))

import time
import json
import numpy as np

import torch

from sentence_transformers import SentenceTransformer, util

def _load_corpus(fn):
    terms = []
    corpus = []
    with open(fn, 'r', encoding='UTF-8') as fp:
        items = json.load(fp)
    for item in items:
        id = item['Id']
        name = item['Name'] or ''
        desc = item['Desc']
        syns = item['Synonyms']
        terms.append((id, name))
        corpus.append(name.lower().replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('-', ' ').replace('(', ' ').replace(')', ' '))
        if desc:
            terms.append((id, name))
            corpus.append(desc.lower())
        if syns:
          for synm in syns:
              terms.append((id, name))
              corpus.append(synm.lower())
    return corpus, terms

def _save_embeddings(fn, embeddings):
    np.save(fn, embeddings)

def _load_embeddings(fn):
    return np.load(fn)

def search(embedder, corpus_embeddings, txt, top_k = 10):
    txt = txt.lower()
    query_embedding = embedder.encode(txt, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    return torch.topk(cos_scores, k=top_k)

def print_results(results, terms):
    scores, indexs = results
    for score, index in zip(scores, indexs):
        print(float(score), *terms[int(index)], sep='\t')

#
#   BUILD
#

PATH = '_data/'
OUTPUT = '_output/'

def build_embedder(model, terms_path, term_type, lang):
  embedder = SentenceTransformer(model)
  corpus, terms = _load_corpus(terms_path)
  corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
  _save_embeddings(OUTPUT + F'{model}-{term_type}-{lang}', corpus_embeddings.to('cpu').numpy())

build_embedder('paraphrase-MiniLM-L6-v2', PATH + 'symptom-terms-en.json', 'symptoms', 'en')
#build_embedder('paraphrase-MiniLM-L6-v2', PATH + 'disease-terms-en.json', 'diseases', 'en')
#build_embedder('paraphrase-multilingual-MiniLM-L12-v2', PATH + 'symptom-terms-es.json', 'symptoms', 'es')
#build_embedder('paraphrase-multilingual-MiniLM-L12-v2', PATH + 'disease-terms-es.json', 'diseases', 'es')


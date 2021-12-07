import json
import numpy as np

import torch

from sentence_transformers import SentenceTransformer, util

class Engine():
    def __init__(self, lang='en'):
        if lang == 'en':
            self.embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
            self.symptoms_embeddings = np.load('_embs/symptoms-en.npy')
            self.diseases_embeddings = np.load('_embs/diseases-en.npy')
            _, self.symptom_indexs = self._load_corpus('_data/symptom-terms-en.json')
            _, self.disease_indexs = self._load_corpus('_data/disease-terms-en.json')
        else:
            self.embedder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
            self.symptoms_embeddings = np.load('_embs/symptoms-es.npy')
            self.diseases_embeddings = np.load('_embs/diseases-es.npy')
            _, self.symptom_indexs = self._load_corpus('_data/symptom-terms-es.json')
            _, self.disease_indexs = self._load_corpus('_data/disease-terms-es.json')

    def _load_corpus(self, fn):
        indexs = []
        corpus = []
        with open(fn, 'r', encoding='UTF-8') as fp:
            terms = json.load(fp)
        for term in terms:
            id = term['Id']
            name = term['Name']
            desc = term['Desc']
            syns = term['Synonyms']
            indexs.append(id)
            #corpus.append(name)
            if desc:
                indexs.append(id)
                #corpus.append(desc)
            if syns:
                for syn in syns:
                    indexs.append(id)
                    #corpus.append(syn)
        return corpus, indexs

    def search_symptoms(self, txt, top_k = 10):
        txt = txt.lower()
        query_embedding = self.embedder.encode(txt, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, self.symptoms_embeddings)[0]
        return torch.topk(cos_scores, k=top_k * 2)

    def search_diseases(self, txt, top_k = 10):
        txt = txt.lower()
        query_embedding = self.embedder.encode(txt, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, self.diseases_embeddings)[0]
        return torch.topk(cos_scores, k=top_k * 2)

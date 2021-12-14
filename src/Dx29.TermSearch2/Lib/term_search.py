import time

from .dictionary import Dictionary
from .engine import Engine

SYMPTOM_TERMS = {
        'en' : '_data/symptom-terms-en.json',
        'es' : '_data/symptom-terms-es.json'
    }

DISEASE_TERMS = {
        'en' : '_data/disease-terms-en.json',
        'es' : '_data/disease-terms-es.json'
    }

class TermSearch():
    def __init__(self, lang):
        t0 = time.time()
        self.symptoms = Dictionary(SYMPTOM_TERMS[lang])
        self.diseases = Dictionary(DISEASE_TERMS[lang])
        self.engine = Engine(lang)
        print('Loaded in ', time.time() - t0, 'secs')

    def search_symptoms(self, query, count = 10):
        words, left = self._get_words(query, self.symptoms)

        results = {}
        for word in words:
            str = (left + ' ' + word).strip().lower()
            vals, keys = self.engine.search_symptoms(str, count)
            for tk, tv in zip(keys, vals):
                k = self.engine.symptom_indexs[int(tk.numpy())]
                v = float(tv.numpy())
                #print(k, v)
                if k in results:
                    results[k] = max(v, results[k])
                else:
                    results[k] = v

        sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        return [self.symptoms.terms[item] for item in list(sorted_results)[:count]]

    def search_diseases(self, query, count = 10):
        words, left = self._get_words(query, self.diseases)

        results = {}
        for word in words:
            str = (left + ' ' + word).strip().lower()
            vals, keys = self.engine.search_diseases(str, count)
            for tk, tv in zip(keys, vals):
                k = self.engine.disease_indexs[int(tk.numpy())]
                v = float(tv.numpy())
                #print(k, v)
                if k in results:
                    results[k] = max(v, results[k])
                else:
                    results[k] = v

        sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        return [self.diseases.terms[item] for item in list(sorted_results)[:count]]

    def search_diseases_prefix(self, query, prefix, count = 10):
        words, left = self._get_words(query, self.diseases)

        results = {}
        for word in words:
            str = (left + ' ' + word).strip().lower()
            vals, keys = self.engine.search_diseases(str, count)
            for tk, tv in zip(keys, vals):
                k = self.engine.disease_indexs[int(tk.numpy())]
                v = float(tv.numpy())
                #print(k, v)
                if k in results:
                    results[k] = max(v, results[k])
                else:
                    results[k] = v

            str = (left + ' ' + word).strip().lower()
            str = prefix + ' ' + str
            vals, keys = self.engine.search_diseases(str, count)
            for tk, tv in zip(keys, vals):
                k = self.engine.disease_indexs[int(tk.numpy())]
                v = float(tv.numpy())
                #print(k, v)
                if k in results:
                    results[k] = max(v, results[k])
                else:
                    results[k] = v

        sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        return [self.diseases.terms[item] for item in list(sorted_results)[:count]]

    def _get_words(self, query, dic):
        words = [w for w in query.split(' ') if len(w) > 0]
        left = ' '.join(words[:-1])
        ends = words[-1].lower()
        words = [ws[0] for ws in dic.get_words(ends)[:3]]
        words.append(ends)
        words = list(dict.fromkeys(words))
        words.sort(key=lambda x: len(x))
        print(words)
        return words, left

    def search_symptoms_ids(self, query, count = 10):
        res = []
        query = query.upper()
        for id in self.symptoms.ids:
            if id.startswith(query):
                res.append(self.symptoms.terms[id])
                count -= 1
                if count == 0:
                    break
        return res

    def search_diseases_ids(self, query, count = 10):
        res = []
        query = query.upper()
        for id in self.diseases.ids:
            if id.startswith(query):
                res.append(self.diseases.terms[id])
                count -= 1
                if count == 0:
                    break
        return res

import json

class Dictionary():
    def __init__(self, fn):
        self.words, self.ids, self.terms = self._load_words(fn)

    def _load_words(self, fn):
        dic = {}
        terms = {}
        with open(fn, 'r', encoding='UTF-8') as fp:
            items = json.load(fp)
        for item in items:
            id = item['Id']
            name = item['Name'].rstrip('.')
            desc = item['Desc'] or name
            syns = item['Synonyms'] or []
            term = { 'id': id, 'name': name, 'desc': desc, 'synonyms': syns }
            self._append_words(dic, name)
            self._append_words(dic, desc)
            for syn in syns:
                self._append_words(dic, syn)
            terms[id] = term
        ids = list(terms)
        ids.sort()
        return dic, ids, terms

    def _append_words(self, dic, txt):
        if txt:
            txt = txt.lower().replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('-', ' ').replace('(', ' ').replace(')', ' ')
            words = txt.lower().split(' ')
            for word in words:
                if len(word) > 1:
                    if word in dic:
                        dic[word] += 1
                    else:
                        dic[word] = 1

    def get_words(self, word_piece):
        items = []
        for word in self.words:
            if word.startswith(word_piece):
                items.append((word, self.words[word]))
        items.sort(key=lambda x: x[1], reverse=True)
        return items


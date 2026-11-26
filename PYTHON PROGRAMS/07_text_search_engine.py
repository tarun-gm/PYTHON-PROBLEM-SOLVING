import re
from collections import defaultdict


class SearchIndex:
    def __init__(self):
        self.documents = {}
        self.index = defaultdict(set)

    def add(self, document_id, text):
        self.remove(document_id)
        self.documents[document_id] = text
        for token in set(re.findall(r"[a-z0-9]+", text.lower())):
            self.index[token].add(document_id)

    def remove(self, document_id):
        old = self.documents.pop(document_id, None)
        if old is None:
            return
        for token in set(re.findall(r"[a-z0-9]+", old.lower())):
            self.index[token].discard(document_id)

    def search(self, query):
        terms = set(re.findall(r"[a-z0-9]+", query.lower()))
        if not terms:
            return []
        matches = set.intersection(*(self.index.get(term, set()) for term in terms))
        return sorted(matches)


if __name__ == "__main__":
    engine = SearchIndex()
    engine.add("doc-1", "Python supports automation and data analysis")
    engine.add("doc-2", "Data structures improve search algorithms")
    print(engine.search("data analysis"))

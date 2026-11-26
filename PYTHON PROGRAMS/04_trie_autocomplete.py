class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            node = node.children.setdefault(char, TrieNode())
        node.terminal = True

    def search(self, word):
        node = self._walk(word)
        return bool(node and node.terminal)

    def _walk(self, prefix):
        node = self.root
        for char in prefix.lower():
            node = node.children.get(char)
            if node is None:
                return None
        return node

    def autocomplete(self, prefix, limit=10):
        node = self._walk(prefix)
        if node is None:
            return []
        output = []

        def visit(current, word):
            if len(output) >= limit:
                return
            if current.terminal:
                output.append(word)
            for char in sorted(current.children):
                visit(current.children[char], word + char)

        visit(node, prefix.lower())
        return output


if __name__ == "__main__":
    trie = Trie()
    for word in ["python", "pytorch", "pycharm", "pandas", "programming"]:
        trie.insert(word)
    print(trie.autocomplete("py"))

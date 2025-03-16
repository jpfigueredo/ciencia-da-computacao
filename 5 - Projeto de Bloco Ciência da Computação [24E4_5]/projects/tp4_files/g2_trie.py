class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def display_words(self):
        words = []
        self._collect_words(self.root, "", words)
        print("Palavras no Trie:", words)
    
    def _collect_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

    def autocomplete(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        suggestions = []
        self._collect_words(current, prefix, suggestions)
        return suggestions

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete = _delete(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            return False
        
        return _delete(self.root, word, 0)


if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "casamento", "casulo", "cachorro"]
    
    for palavra in palavras:
        trie.insert(palavra)
    
    print("\n=== Antes da Remoção ===")
    print("Autocomplete 'cas':", trie.autocomplete("cas"))
    trie.delete("casa")
    print("\n=== Após Remover 'casa' ===")
    print("Busca 'casa':", trie.search("casa"))
    print("Autocomplete 'cas':", trie.autocomplete("cas"))
    print("Estrutura do Trie após remoção:")
    trie.display_words()
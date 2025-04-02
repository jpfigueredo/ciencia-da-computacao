class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixo = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def inserir(self, prefixo):
        node = self.root
        for parte in prefixo.split(':'):
            if parte not in node.children:
                node.children[parte] = TrieNode()
            node = node.children[parte]
        node.prefixo = prefixo

    def buscar(self, ip):
        node = self.root
        for parte in ip.split(':'):
            if parte in node.children:
                node = node.children[parte]
            else:
                return None
        return node.prefixo

# Exemplo de uso
trie = Trie()
trie.inserir("2001:db8::/32")
trie.inserir("2001:db8:1234::/48")

ip = "2001:db8:1234:5678::1"
prefixo = trie.buscar(ip)
if prefixo:
    print(f"O IP {ip} corresponde ao prefixo {prefixo}.")
else:
    print(f"O IP {ip} NÃO corresponde a nenhum prefixo.")

class Node:
    """Representa um nó na árvore binária de busca."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Implementação de uma árvore binária de busca (BST)."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insere um novo nó com a chave especificada na árvore."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def search(self, key):
        """Procura por um nó com a chave especificada na árvore."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            return False
        if current_node.key == key:
            return True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

bst = BinarySearchTree()

prices = [100, 50, 150, 30, 70, 130, 170]
for price in prices:
    bst.insert(price)

price_to_search = 70
found = bst.search(price_to_search)

if found:
    print(f"O preço {price_to_search} está disponível.")
else:
    print(f"O preço {price_to_search} não está disponível.")

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
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

    def find_min(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.key:
            node.right = self._remove_recursive(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self.find_min(node.right)
                node.key = min_node.key
                node.right = self._remove_recursive(node.right, min_node.key)

        return node

    def inorder(self):
        """Retorna a árvore em ordem crescente."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Função recursiva para realizar a travessia em ordem."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

bst = BinarySearchTree()

codes = [45, 25, 65, 20, 30, 60, 70]
for code in codes:
    bst.insert(code)

print("Árvore original (ordem crescente):", bst.inorder())

bst.remove(20)
print("Após remover 20 (nó folha):", bst.inorder())

bst.remove(25)
print("Após remover 25 (nó com um filho):", bst.inorder())

bst.remove(45)
print("Após remover 45 (nó com dois filhos):", bst.inorder())

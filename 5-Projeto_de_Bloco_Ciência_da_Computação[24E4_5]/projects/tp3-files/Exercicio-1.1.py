class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.value)
            self._in_order_traversal(node.right, result)

    def pre_order(self):
        result = []
        self._pre_order_traversal(self.root, result)
        return result

    def _pre_order_traversal(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)

    def post_order(self):
        result = []
        self._post_order_traversal(self.root, result)
        return result

    def _post_order_traversal(self, node, result):
        if node is not None:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.value)

# Exemplo de uso
if __name__ == "__main__":
    bst = BST()
    elementos = [50, 30, 70, 20, 40, 60, 80]
    for elem in elementos:
        bst.insert(elem)

    print("In-order:", ' '.join(map(str, bst.in_order())))
    print("Pre-order:", ' '.join(map(str, bst.pre_order())))
    print("Post-order:", ' '.join(map(str, bst.post_order())))
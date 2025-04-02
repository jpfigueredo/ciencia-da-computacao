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

    def find_min(self):
        current_node = self.root
        if not current_node:
            return None
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.key

    def find_max(self):
        current_node = self.root
        if not current_node:
            return None
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.key


bst = BinarySearchTree()

grades = [85, 70, 95, 60, 75, 90, 100]
for grade in grades:
    bst.insert(grade)

min_grade = bst.find_min()
max_grade = bst.find_max()
print(f"Nota mínima: {min_grade}")
print(f"Nota máxima: {max_grade}")

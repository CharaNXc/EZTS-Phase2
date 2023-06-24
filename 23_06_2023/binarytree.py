class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

    def traverse_inorder(self):
        self._traverse_inorder_recursive(self.root)

    def _traverse_inorder_recursive(self, node):
        if node is not None:
            self._traverse_inorder_recursive(node.left)
            print(node.data, end=" ")
            self._traverse_inorder_recursive(node.right)


# Usage example
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print("Inorder traversal:")
tree.traverse_inorder()

# Search for a value
search_value = 4
result = tree.search(search_value)
if result is not None:
    print(f"\nFound {search_value} in the tree!")
else:
    print(f"\n{search_value} not found in the tree.")

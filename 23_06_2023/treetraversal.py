class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def preorder_traversal(self):
        print(self.name)
        for child in self.children:
            child.preorder_traversal()

    def inorder_traversal(self):
        if len(self.children) > 0:
            self.children[0].inorder_traversal()
        print(self.name)
        if len(self.children) > 1:
            self.children[1].inorder_traversal()

    def postorder_traversal(self):
        for child in self.children:
            child.postorder_traversal()
        print(self.name)


# Creating the family tree
grandparent = Node("Grandparent")
parent1 = Node("Parent 1")
parent2 = Node("Parent 2")
child1 = Node("Child 1")
child2 = Node("Child 2")

grandparent.add_child(parent1)
grandparent.add_child(parent2)
parent1.add_child(child1)
parent2.add_child(child2)

# Displaying the family tree using different traversal methods
print("Preorder Traversal:")
grandparent.preorder_traversal()
print()

print("Inorder Traversal:")
grandparent.inorder_traversal()
print()

print("Postorder Traversal:")
grandparent.postorder_traversal()

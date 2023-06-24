class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        indent = " " * level
        print(indent + self.name)
        for child in self.children:
            child.display(level + 1)


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

# Displaying the family tree
grandparent.display()

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    # Function to compare two linked lists for equality
    def is_equal(self, other_list):
        current_self = self.head
        current_other = other_list.head

        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next

        # If both lists have been traversed completely and no inequality found
        if current_self is None and current_other is None:
            return True

        # If one list has been traversed completely but the other still has elements
        return False


# Create the first linked list
list1 = LinkedList()
n1 = int(input("Enter the number of elements for the first linked list: "))
print("Enter the elements:")
for _ in range(n1):
    element = int(input())
    list1.append(element)

# Create the second linked list
list2 = LinkedList()
n2 = int(input("Enter the number of elements for the second linked list: "))
print("Enter the elements:")
for _ in range(n2):
    element = int(input())
    list2.append(element)

# Compare the two linked lists for equality
if list1.is_equal(list2):
    print("The linked lists are equal.")
else:
    print("The linked lists are not equal.")

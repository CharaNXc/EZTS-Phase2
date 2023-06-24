    #STACK IS LIFO EZ AF
stack = []

def push():
    element = int(input("Enter the Element:"))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is Empty")
    else:
        e = stack.pop()
        print("Removed Element:", e)
        print(stack)
def display():
    if not stack:
        print("Stack is Empty")
    else:
        print(stack)

while True:
    print("Select operation\n1.Push\n2.Pop\n3.Display\n4.Exit")
    choice = int(input())
    match choice:
        case 1:
            push()
        case 2:
            pop_element()
        case 3:
            display()
        case 4:
            exit()
            
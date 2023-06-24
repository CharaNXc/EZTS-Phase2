# Create a stack with user input, extract only even numbers and print

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


def display_even():
    if not stack:
        print("stack is Empty")
    else:
        for s in stack:
            if s % 2 == 0:
                print(s, end=" ")


def display_odd():
    if not stack:
        print("stack is Empty")
    else:
        for s in stack:
            if s % 2 != 0:
                print(s, end=" ")


while True:
    print(
        "Select operation\n1.Push\n2.Pop\n3.Display\n4.Display Even\n5.Display Odd\n6.Exit"
    )
    choice = int(input())
    match choice:
        case 1:
            push()
        case 2:
            pop_element()
        case 3:
            display()
        case 4:
            display_even()
        case 5:
            display_odd()
        case 6:
            exit()

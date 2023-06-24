def push():
    q = int(input("Enter the stack element"))
    l.append(q)


def pop():
    if len(l) != 0:
        print("The Element popped is ", l.pop())
    else:
        print("The Element stack is empty")


l = []
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Peek")
    c = int(input("Enter your Choice"))
    if c == 1:
        push()
    elif c == 2:
        pop()
    elif c == 3:
        if len(l) == 0:
            print("The Stack is empty")
        else:
            print("The Elements in the Stack are ", l)
    elif c == 4:
        if len(l) != 0:
            print("The Element on the top of the Stack is:", l[-1])
        else:
            print("The Stack is empty")
    else:
        print("Enter the valid choice")

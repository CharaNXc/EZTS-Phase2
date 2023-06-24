queue = []


def enqueue():
    element = input("Enter Element")
    queue.append(element)
    print(element, "is added in Queue")


def dequeue():
    if not queue:
        print("Queue is Empty")
    else:
        e = queue.pop(0)
        print("Removed Element", e)


def display():
    print(queue)


while True:
    print("Select Operation\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        exit()
    else:
        print("Invalid Input")

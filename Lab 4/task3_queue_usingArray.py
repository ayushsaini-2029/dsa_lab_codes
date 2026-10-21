# LAB ASSIGNMENT 4
# Task 3: Queue using Array


# --------------------------------
# Queue Settings
# --------------------------------

MAX_SIZE = 5

queue = [None] * MAX_SIZE

front = -1
rear = -1


# --------------------------------
# Enqueue Operation
# --------------------------------

def enqueue(value):
    global front, rear

    # Check if queue is full
    if rear == MAX_SIZE - 1:
        print("Queue Overflow! Queue is full.")

    else:
        # First element
        if front == -1:
            front = 0

        rear = rear + 1
        queue[rear] = value

        print(value, "inserted into the queue.")


# --------------------------------
# Dequeue Operation
# --------------------------------

def dequeue():
    global front, rear

    # Check if queue is empty
    if front == -1 or front > rear:
        print("Queue Underflow! Queue is empty.")

    else:
        value = queue[front]

        queue[front] = None

        front = front + 1

        print(value, "removed from the queue.")

        # Reset queue when it becomes empty
        if front > rear:
            front = -1
            rear = -1


# --------------------------------
# Display Operation
# --------------------------------

def display():

    if front == -1:
        print("Queue is empty.")

    else:
        print("Queue elements:")

        for i in range(front, rear + 1):
            print(queue[i], end=" ")

        print()


# --------------------------------
# Menu
# --------------------------------

while True:

    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("Enter value to enqueue: "))
        enqueue(value)

    elif choice == 2:

        dequeue()

    elif choice == 3:

        display()

    elif choice == 4:

        print("Program ended.")
        break

    else:

        print("Invalid choice. Please try again.")
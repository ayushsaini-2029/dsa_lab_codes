# LAB ASSIGNMENT 4
# Task 4: Queue using Dynamic Pointer-Linked Nodes


# --------------------------------
# Node Class
# --------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# --------------------------------
# Queue Variables
# --------------------------------

front = None
rear = None


# --------------------------------
# Enqueue Operation
# --------------------------------

def enqueue(value):
    global front, rear

    # Create a new node
    new_node = Node(value)

    # If queue is empty
    if front is None:
        front = new_node
        rear = new_node

    else:
        # Add new node after rear
        rear.next = new_node

        # Move rear to the new node
        rear = new_node

    print(value, "inserted into the queue.")


# --------------------------------
# Dequeue Operation
# --------------------------------

def dequeue():
    global front, rear

    # Check if queue is empty
    if front is None:
        print("Queue Underflow! Queue is empty.")

    else:
        value = front.data

        # Move front to the next node
        front = front.next

        # If queue becomes empty
        if front is None:
            rear = None

        print(value, "removed from the queue.")


# --------------------------------
# Display Operation
# --------------------------------

def display():

    if front is None:
        print("Queue is empty.")

    else:
        print("Queue elements:")

        current = front

        while current is not None:
            print(current.data, end=" ")
            current = current.next

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
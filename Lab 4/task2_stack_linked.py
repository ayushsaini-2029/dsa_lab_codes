# LAB ASSIGNMENT 4
# Task 2: Stack using Dynamic Pointer-Linked Nodes


# --------------------------------
# Node Class
# --------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Top of the stack
top = None


# --------------------------------
# Push Operation
# --------------------------------

def push(value):
    global top

    # Create a new node
    new_node = Node(value)

    # New node points to the current top
    new_node.next = top

    # New node becomes the new top
    top = new_node

    print(value, "pushed into the stack.")


# --------------------------------
# Pop Operation
# --------------------------------

def pop():
    global top

    if top is None:
        print("Stack Underflow! Stack is empty.")
    else:
        value = top.data

        # Move top to the next node
        top = top.next

        print(value, "popped from the stack.")


# --------------------------------
# Display Operation
# --------------------------------

def display():

    if top is None:
        print("Stack is empty.")
    else:
        print("Stack elements:")

        current = top

        while current is not None:
            print(current.data)
            current = current.next


# --------------------------------
# Menu
# --------------------------------

while True:

    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("Enter value to push: "))
        push(value)

    elif choice == 2:

        pop()

    elif choice == 3:

        display()

    elif choice == 4:

        print("Program ended.")
        break

    else:

        print("Invalid choice. Please try again.")
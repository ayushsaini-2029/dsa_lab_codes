# LAB ASSIGNMENT 4
# Task 1: Stack using Static Array


# Maximum size of stack
MAX_SIZE = 5

# Create static array
stack = [None] * MAX_SIZE

# Top indicates the position of the top element
top = -1


# --------------------------------
# Push Operation
# --------------------------------

def push(value):
    global top

    if top == MAX_SIZE - 1:
        print("Stack Overflow! Stack is full.")
    else:
        top = top + 1
        stack[top] = value
        print(value, "pushed into the stack.")


# --------------------------------
# Pop Operation
# --------------------------------

def pop():
    global top

    if top == -1:
        print("Stack Underflow! Stack is empty.")
    else:
        value = stack[top]
        stack[top] = None
        top = top - 1
        print(value, "popped from the stack.")


# --------------------------------
# Display Operation
# --------------------------------

def display():
    if top == -1:
        print("Stack is empty.")
    else:
        print("Stack elements:")

        for i in range(top, -1, -1):
            print(stack[i])


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
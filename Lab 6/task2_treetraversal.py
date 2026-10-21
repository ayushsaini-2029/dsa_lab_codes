# Task 2 - Part B
# Iterative Tree Traversals using Stack
# Inorder, Preorder and Postorder


# --------------------------------
# Node Class
# --------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# --------------------------------
# Create Binary Tree
# --------------------------------

root = Node(10)

root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(7)


# --------------------------------
# Inorder Traversal - Iterative
# Left -> Root -> Right
# --------------------------------

def inorder_iterative(root):

    stack = []
    current = root

    while current is not None or len(stack) > 0:

        # Go as far left as possible
        while current is not None:
            stack.append(current)
            current = current.left

        # Get the last node from stack
        current = stack.pop()

        # Visit the node
        print(current.data, end=" ")

        # Move to the right subtree
        current = current.right


# --------------------------------
# Preorder Traversal - Iterative
# Root -> Left -> Right
# --------------------------------

def preorder_iterative(root):

    if root is None:
        return

    stack = [root]

    while len(stack) > 0:

        # Remove top node
        current = stack.pop()

        # Visit the node
        print(current.data, end=" ")

        # Add right first
        if current.right is not None:
            stack.append(current.right)

        # Add left second
        if current.left is not None:
            stack.append(current.left)


# --------------------------------
# Postorder Traversal - Iterative
# Left -> Right -> Root
# --------------------------------

def postorder_iterative(root):

    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while len(stack1) > 0:

        current = stack1.pop()
        stack2.append(current)

        # Add left child
        if current.left is not None:
            stack1.append(current.left)

        # Add right child
        if current.right is not None:
            stack1.append(current.right)

    # Print nodes in reverse order
    while len(stack2) > 0:
        current = stack2.pop()
        print(current.data, end=" ")


# --------------------------------
# Display Tree
# --------------------------------

print("Binary Tree:")
print("        10")
print("       /  \\")
print("      5    20")
print("     / \\")
print("    3   7")


# --------------------------------
# Display Traversals
# --------------------------------

print("\nInorder Traversal (Iterative):")
inorder_iterative(root)

print("\n\nPreorder Traversal (Iterative):")
preorder_iterative(root)

print("\n\nPostorder Traversal (Iterative):")
postorder_iterative(root)

print()
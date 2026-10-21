# Task 2 - Part A
# Recursive Tree Traversals
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
# Inorder Traversal
# Left -> Root -> Right
# --------------------------------

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# --------------------------------
# Preorder Traversal
# Root -> Left -> Right
# --------------------------------

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# --------------------------------
# Postorder Traversal
# Left -> Right -> Root
# --------------------------------

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# --------------------------------
# Display Results
# --------------------------------

print("Binary Tree:")
print("        10")
print("       /  \\")
print("      5    20")
print("     / \\")
print("    3   7")

print("\nInorder Traversal:")
inorder(root)

print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()
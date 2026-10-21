# Task 1: Tree Construction
# Create a binary tree using nodes with left and right references


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the root node
root = Node(10)

# Create left and right children of root
root.left = Node(5)
root.right = Node(20)

# Create children of node 5
root.left.left = Node(3)
root.left.right = Node(7)


# Displaying the tree structure
print("Binary Tree:")
print("        ", root.data)
print("       /    \\")
print("      ", root.left.data, "   ", root.right.data)
print("     /  \\")
print("    ", root.left.left.data, "  ", root.left.right.data)
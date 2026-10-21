"""Lab 8 - Task 1: Binary Search Tree Operations"""

from __future__ import annotations

from typing import List, Optional


class BSTNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[BSTNode], key: int) -> BSTNode:
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key: int) -> tuple[bool, List[int]]:
        path: List[int] = []
        current = self.root

        while current is not None:
            path.append(current.key)
            if key == current.key:
                return True, path
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return False, path

    def inorder(self) -> List[int]:
        result: List[int] = []

        def walk(node: Optional[BSTNode]) -> None:
            if node is None:
                return
            walk(node.left)
            result.append(node.key)
            walk(node.right)

        walk(self.root)
        return result

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[BSTNode], key: int) -> Optional[BSTNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
            return node

        if key > node.key:
            node.right = self._delete(node.right, key)
            return node

        # Node with no children
        if node.left is None:
            return node.right

        # Node with one child
        if node.right is None:
            return node.left

        # Node with two children: replace with inorder successor
        successor = self._min_value_node(node.right)
        node.key = successor.key
        node.right = self._delete(node.right, successor.key)
        return node

    @staticmethod
    def _min_value_node(node: BSTNode) -> BSTNode:
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25]

    for value in values:
        bst.insert(value)

    print("BST inorder traversal:", bst.inorder())
    print("Search for 25:", bst.search(25))
    print("Search for 99:", bst.search(99))

    bst.delete(30)
    print("After deleting 30:", bst.inorder())


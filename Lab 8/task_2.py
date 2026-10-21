"""Lab 8 - Task 2: AVL Tree Rotations"""

from __future__ import annotations

from typing import List, Optional


class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node is not None else 0

    def _balance_factor(self, node: Optional[AVLNode]) -> int:
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, node: AVLNode) -> AVLNode:
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root

    def _right_rotate(self, node: AVLNode) -> AVLNode:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root

    def _left_right_rotate(self, node: AVLNode) -> AVLNode:
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _right_left_rotate(self, node: AVLNode) -> AVLNode:
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance_factor(node)

        # Left Left (LL)
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        # Right Right (RR)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        # Left Right (LR)
        if balance > 1 and key > node.left.key:
            return self._left_right_rotate(node)

        # Right Left (RL)
        if balance < -1 and key < node.right.key:
            return self._right_left_rotate(node)

        return node

    def inorder(self) -> List[int]:
        result: List[int] = []

        def walk(node: Optional[AVLNode]) -> None:
            if node is None:
                return
            walk(node.left)
            result.append(node.key)
            walk(node.right)

        walk(self.root)
        return result

    def print_balance(self) -> None:
        def walk(node: Optional[AVLNode], depth: int = 0) -> None:
            if node is None:
                return
            print(f"{'  ' * depth}Node {node.key}: balance={self._balance_factor(node)}")
            walk(node.left, depth + 1)
            walk(node.right, depth + 1)

        walk(self.root)


if __name__ == "__main__":
    avl = AVLTree()
    values = [30, 20, 10, 25, 40, 50, 35]

    for value in values:
        avl.insert(value)
        print(f"After inserting {value}: {avl.inorder()}")

    print("\nFinal AVL inorder traversal:", avl.inorder())
    print("\nBalance factors:")
    avl.print_balance()

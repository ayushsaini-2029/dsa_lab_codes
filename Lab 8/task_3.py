"""Lab 8 - Task 3: B-Tree Insertion Simulator (Order 3)"""

from __future__ import annotations

from typing import List, Optional


class BTreeNode:
    def __init__(self, is_leaf: bool = True):
        self.keys: List[int] = []
        self.children: List["BTreeNode"] = []
        self.is_leaf = is_leaf


class BTree:
    def __init__(self, order: int = 3):
        self.order = order
        self.root = BTreeNode(is_leaf=True)

    def insert(self, key: int) -> None:
        if len(self.root.keys) >= self.order - 1:
            new_root = BTreeNode(is_leaf=False)
            new_root.children.append(self.root)
            self.root = new_root
            self._split_child(self.root, 0)
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node: BTreeNode, key: int) -> None:
        i = len(node.keys) - 1

        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
            return

        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1

        if len(node.children[i].keys) >= self.order - 1:
            self._split_child(node, i)
            if key > node.keys[i]:
                i += 1

        self._insert_non_full(node.children[i], key)

    def _split_child(self, parent: BTreeNode, index: int) -> None:
        child = parent.children[index]
        mid = len(child.keys) // 2
        median = child.keys[mid]

        new_child = BTreeNode(is_leaf=child.is_leaf)
        new_child.keys = child.keys[mid + 1 :]
        child.keys = child.keys[:mid]

        if not child.is_leaf:
            new_child.children = child.children[mid + 1 :]
            child.children = child.children[: mid + 1]

        parent.keys.insert(index, median)
        parent.children.insert(index + 1, new_child)

    def print_tree(self, node: Optional[BTreeNode] = None, level: int = 0) -> None:
        if node is None:
            node = self.root
        print(f"{'  ' * level}Level {level}: {node.keys}")
        if not node.is_leaf:
            for child in node.children:
                self.print_tree(child, level + 1)


if __name__ == "__main__":
    btree = BTree(order=3)
    values = [10, 20, 5, 6, 12, 30, 7, 17, 3, 8, 19, 25]

    for value in values:
        btree.insert(value)
        print(f"After inserting {value}:")
        btree.print_tree()
        print("-" * 40)

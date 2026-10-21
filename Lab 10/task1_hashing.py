class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class OpenHash:
    def __init__(self, n):
        self.n = n
        self.table = [None] * n

    def hash(self, k):
        return k % self.n

    def insert(self, k):
        i = self.hash(k)
        node = Node(k)
        node.next = self.table[i]
        self.table[i] = node

    def search(self, k):
        i = self.hash(k)
        p = self.table[i]
        while p and p.val != k:
            p = p.next
        return p is not None

    def delete(self, k):
        i = self.hash(k)
        p = self.table[i]
        if p and p.val == k:
            self.table[i] = p.next
            return
        while p and p.next and p.next.val != k:
            p = p.next
        if p and p.next:
            p.next = p.next.next


class ClosedHash:
    def __init__(self, n):
        self.n = n
        self.table = [None] * n
        self.count = 0

    def hash(self, k):
        return k % self.n

    def rehash(self):
        old = self.table
        self.n *= 2
        self.table = [None] * self.n
        self.count = 0
        for x in old:
            if x is not None:
                self.insert(x)

    def insert(self, k):
        if self.count * 100 // self.n >= 70:
            self.rehash()
        i = self.hash(k)
        while self.table[i] is not None:
            i = (i + 1) % self.n
        self.table[i] = k
        self.count += 1

    def search(self, k):
        i = self.hash(k)
        for _ in range(self.n):
            if self.table[i] == k:
                return True
            if self.table[i] is None:
                return False
            i = (i + 1) % self.n
        return False


# Example
oh = OpenHash(5)
for x in [12, 15, 25, 37]:
    oh.insert(x)
print("Open Hash Search 25:", oh.search(25))

ch = ClosedHash(5)
for x in [12, 15, 25, 37, 42]:
    ch.insert(x)
print("Closed Hash Search 42:", ch.search(42))

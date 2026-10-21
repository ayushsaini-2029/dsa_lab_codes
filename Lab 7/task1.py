import heapq


# Node for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    # Leaf node
    if root.char is not None:
        codes[root.char] = code
        return codes

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)

    return codes


# Build Huffman Tree
def huffman_encoding(characters, frequencies):

    heap = []

    # Create nodes and add them to min-heap
    for char, freq in zip(characters, frequencies):
        node = Node(char, freq)
        heapq.heappush(heap, node)

    # Combine two lowest-frequency nodes
    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)

        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # Root of Huffman Tree
    root = heap[0]

    # Generate codes
    codes = generate_codes(root)

    return codes


# -------------------------
# Main Program
# -------------------------

characters = ['A', 'B', 'C', 'D', 'E', 'F']
frequencies = [5, 9, 12, 13, 16, 45]

codes = huffman_encoding(characters, frequencies)

print("Huffman Codes:")

for char in characters:
    print(char, ":", codes[char])
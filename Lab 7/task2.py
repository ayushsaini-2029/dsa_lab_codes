import heapq


def optimal_merge(file_sizes):

    # Create a min-heap
    heapq.heapify(file_sizes)

    total_cost = 0

    print("Merge Sequence:")

    while len(file_sizes) > 1:

        # Remove two smallest files
        first = heapq.heappop(file_sizes)
        second = heapq.heappop(file_sizes)

        # Merge them
        merged = first + second

        # Add merge cost
        total_cost += merged

        print(first, "+", second, "=", merged)

        # Insert merged file back
        heapq.heappush(file_sizes, merged)

    return total_cost


# -------------------------
# Main Program
# -------------------------

files = [10, 20, 30, 40]

cost = optimal_merge(files)

print("\nMinimum Total Merge Cost:", cost)
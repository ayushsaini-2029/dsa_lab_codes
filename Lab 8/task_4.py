"""Lab 8 - Task 4: Sorting Algorithms"""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bucket_sort(arr: List[float]) -> List[float]:
    if not arr:
        return []

    buckets: List[List[float]] = [[] for _ in range(len(arr))]
    min_value = min(arr)
    max_value = max(arr)

    if max_value == min_value:
        buckets[0].extend(arr)
        return insertion_sort([float(x) for x in buckets[0]])

    range_size = (max_value - min_value) / len(arr)

    for value in arr:
        index = int((value - min_value) / range_size)
        if index == len(arr):
            index = len(arr) - 1
        buckets[index].append(value)

    sorted_values: List[float] = []
    for bucket in buckets:
        sorted_values.extend(insertion_sort(bucket))
    return sorted_values


if __name__ == "__main__":
    print("=== Insertion Sort ===")
    print(insertion_sort([9, 3, 7, 5, 1, 8]))

    print("\n=== Bucket Sort ===")
    print(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))

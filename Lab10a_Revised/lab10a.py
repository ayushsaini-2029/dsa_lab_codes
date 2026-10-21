
def solve():
    t = int(input("Enter number of test cases: "))

    for i in range(t):
        n, k = map(int, input("Enter n and k: ").split())

        arr = list(map(int, input("Enter array elements: ").split()))

        for j in range(n):
            distance = bin(arr[j] ^ k).count('1')
            arr[j] = (distance, arr[j])

        arr.sort()

        for j in range(n):
            arr[j] = arr[j][1]

        print("Sorted array:", *arr)


solve()

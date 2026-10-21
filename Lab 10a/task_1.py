def solve():
    N = int(input())
    nums = list(map(int, input().split()))

    freq = {}

    for num in nums:
        digit_sum = sum(map(int, str(abs(num))))
        freq[digit_sum] = freq.get(digit_sum, 0) + 1

    ans = 0

    # Count ordered pairs (i, j), i != j
    for count in freq.values():
        ans += count * (count - 1)

    print(ans)


solve()
import sys

input = sys.stdin
a, b = input.readline().split()
W = int(a)
n = int(b)

array = [0] + list(map(int, input.readline().split()))

dp = []
for i in range(n + 1):
    new_row = [0] * (W + 1)
    dp.append(new_row)

for i in range(1, n + 1):
    for w in range(1, W + 1):
        dp[i][w] = dp[i - 1][w]
        if array[i] <= w:
            j = w - array[i] if w - array[i] >= 0 else 0
            dp[i][w] = max(dp[i][w], dp[i - 1][j] + array[i])

print(dp[n][W])

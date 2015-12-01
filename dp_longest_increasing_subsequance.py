import sys

input = sys.stdin
n = int(input.readline())
array = list(map(int, input.readline().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if array[i] % array[j] == 0 and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))

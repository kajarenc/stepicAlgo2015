import sys

input = sys.stdin
n = int(input.readline())
array = list(map(int, input.readline().split()))

dp = [array[0]]
if n == 1:
    print(dp[0])
elif n >= 2:
    dp.append(max(array[0] + array[1], array[1]))
for i in range(2, n):
    dp.append(max(dp[i - 1] + array[i], dp[i - 2] + array[i]))
print(dp[-1])

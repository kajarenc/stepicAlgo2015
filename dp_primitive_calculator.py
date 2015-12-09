n = int(input())
dp = [0, 0]
for i in range(2, n + 1):
    doubling = 100000000
    trebling = 100000000
    if i % 2 == 0:
        doubling = dp[i // 2]
    if i % 3 == 0:
        trebling = dp[i // 3]
    increment = dp[i - 1]
    dp.append(min(increment, doubling, trebling) + 1)
print(dp[-1])
res = []
j = n
while j != 1:
    res.append(j)
    if dp[j] == dp[j - 1] + 1:
        j -= 1
    elif j % 2 == 0 and dp[j] == dp[j // 2] + 1:
        j //= 2
    elif j % 3 == 0 and dp[j] == dp[j // 3] + 1:
        j //= 3
res.append(1)
for elem in reversed(res):
    print(elem, end=" ")

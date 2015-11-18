import math

n = input()
n = int(n)

k = int((-1 + math.sqrt(1 + 8 * n)) / 2)

lastTermDiff = int(n - k * (k + 1) / 2)
print(k)
for i in range(1, k):
    print(i, end=" ")
print(k + lastTermDiff)


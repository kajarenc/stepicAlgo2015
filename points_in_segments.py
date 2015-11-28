import sys
from bisect import bisect_left, bisect_right

input = sys.stdin
n, m = map(int, input.readline().split())
left = []
right = []
for i in range(n):
    l, r = map(int, input.readline().split())
    left.append(l)
    right.append(r)
points = map(int, input.readline().split())
left.sort()
right.sort()

res = []
for point in points:
    result = bisect_right(left, point) - bisect_left(right, point)
    print(result, end=" ")

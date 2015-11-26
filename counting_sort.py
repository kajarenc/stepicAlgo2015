import sys

input = sys.stdin
n = int(input.readline())
arr = list(map(int, input.readline().split()))
arr.sort()
for i in range(len(arr)):
    print(arr[i], end=" ")

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin
array = list(map(int, input.readline().split()))
n = array[0]
array = array[1:]
elem_array = list(map(int, input.readline().split()))
k = elem_array[0]
elem_array = elem_array[1:]

for elem in elem_array:
    br = bisect_right(array, elem)
    if bisect_left(array, elem) == br:
        print(-1, end=" ")
    else:
        print(br, end=" ")

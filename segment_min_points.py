import string
import sys

# input = open('1.txt', 'r')
input = sys.stdin
S = []
n = int(input.readline())
for i in range(1, n + 1):
    x, y = map(int, input.readline().split())
    S.append([x, y])

getKey = lambda item: item[1]
res = []
S.sort(key=getKey)

while len(S):
    good_point = S.pop(0)[1]
    res.append(good_point)
    S = [elem for elem in S if not (elem[0] <= good_point <= elem[1])]
print(len(res))
for point in res:
    print(point, end=' ')

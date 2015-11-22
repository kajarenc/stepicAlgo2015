import string
import sys

# input = open('1.txt', 'r')
input = sys.stdin
G = []
n, V = map(int, input.readline().split())
for _ in range(n):
    cost, value = map(int, input.readline().split())
    G.append([cost, value])

getKey = lambda item: float(item[0])/ item[1]
res = 0
G.sort(key=getKey)

i = 0

while V and G:
    current_product = G.pop()
    if V >= current_product[1]:
        V -= current_product[1]
        res += current_product[0]
    elif V < current_product[1]:
        res += V * (current_product[0] / current_product[1])
        V = 0
print(round(res, 8))

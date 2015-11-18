n = input()
n = int(n)

prev = 0
current = 1

for i in range(1, n):
    next = (current + prev) % 10
    prev = current
    current = next

print(current)

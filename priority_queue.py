from queue import PriorityQueue
n = int(input())
pq = PriorityQueue()
for i in range(n):
    s = input()
    if s[0] == "I":
        pq.put(-int(s[7:]))
    else:
        print(-pq.get())

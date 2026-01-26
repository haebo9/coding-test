from collections import deque
n = int(input())
q = deque(range(1, n+1))

while len(q) >= 2: 
    q.popleft()
    temp = q.popleft()
    q.append(temp)

print(q[0])
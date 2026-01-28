import sys
input = sys.stdin.readline

from collections import deque
n = int(input())

result = []
nq = deque(range(1, n+1))
q = deque(map(int, input().strip().split()))

move = q.popleft()
move_n = nq.popleft()
result.append(move_n)

while q: 
    for _ in range(abs(move)):
        if move > 0: 
            q.append(q.popleft())
            nq.append(nq.popleft())
            ck = True
        else: 
            q.appendleft(q.pop())
            nq.appendleft(nq.pop())
            ck = False

    move = (q.pop() if ck else q.popleft())
    move_n = (nq.pop() if ck else nq.popleft())

    result.append(move_n)

print(*result)
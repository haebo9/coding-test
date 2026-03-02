import sys
input = sys.stdin.readline 

from collections import deque
q = deque([])
n = int(input())

for line in sys.stdin: 
    cmd, *x = line.strip().split()
    if cmd == 'push': 
        q.append(x[0])
    elif cmd == 'pop': 
        print(q.popleft() if q else -1)
    elif cmd == 'size': 
        print(len(q))
    elif cmd == 'empty': 
        print(0 if q else 1) 
    elif cmd == 'front': 
        print(q[0] if q else -1) 
    elif cmd == 'back': 
        print(q[-1] if q else -1) 
from collections import deque
import sys

input = sys.stdin.readline
q = deque()

def f_order(order):
    global q
    if order[:4] == 'push':
        order, x = order.split()
        q.append(int(x))
    elif order == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        print(int(not q))
    elif order == 'front':
        if q: print(q[0])
        else: print(-1)
    elif order == 'back':
        if q: print(q[-1])    
        else: print(-1)
    else: 
        print('Incorrect Order')

n = int(input())
for _ in range(n):
    order = input().strip()
    f_order(order)
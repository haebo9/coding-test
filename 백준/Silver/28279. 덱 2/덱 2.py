import sys
from collections import deque

input = sys.stdin.readline
q = deque()

def f_order(order:str):
    global q
    if len(order) > 1: 
        order, x = order.split()
        if order == '1':
            q.appendleft(int(x))
        elif order == '2': 
            q.append(int(x))
    elif order == '3':
        print(q.popleft() if q else -1)
    elif order == '4': 
        print(q.pop() if q else -1)
    elif order == '5': 
        print(len(q))
    elif order == '6': 
        print(1 if not q else 0)
    elif order == '7': 
        print(q[0] if q else -1)
    elif order == '8':
        print(q[-1] if q else -1)
    else: 
        print('error')

for _ in range(int(input())):
    order = input().strip()
    f_order(order)
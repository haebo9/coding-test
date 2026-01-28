import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
A = map(int, input().strip().split())
B = map(int, input().strip().split())
m = int(input())
C = map(int, input().strip().split())

q = deque([b for a,b in zip(A, B) if a==0][::-1]) 
result = []

for c in C:
    q.append(c)
    temp = q.popleft()
    result.append(temp)

print(*result)
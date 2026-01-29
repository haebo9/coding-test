import sys
input = sys.stdin.readline 

import heapq 

q = []

n = int(input())

for _ in range(n):
    num = int(input())
    heapq.heappush(q, num)

while q: 
    print(heapq.heappop(q))
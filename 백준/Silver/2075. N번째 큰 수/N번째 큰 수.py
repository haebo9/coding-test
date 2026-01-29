import sys
input = sys.stdin.readline

import heapq 

n = int(input())
q = []
for l in map(int, input().strip().split()):
    heapq.heappush(q,l)

for _ in range(n-1):
    line = map(int, input().strip().split())
    for l in line: 
        if l > q[0]: 
            heapq.heappop(q)
            heapq.heappush(q, l)
    
print(heapq.heappop(q))
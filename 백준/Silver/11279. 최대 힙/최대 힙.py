import heapq
import sys
input = sys.stdin.readline

hq = []
for _ in range(int(input())):
    x = int(input())
    if x != 0: 
        heapq.heappush(hq,-x)
    else: 
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
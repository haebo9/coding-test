import heapq
import sys
input = sys.stdin.readline

maxh = [] # 음수 
minh = [] # 양수

for _ in range(int(input())):
    x = int(input())
    if x > 0:
        heapq.heappush(minh, x)
    elif x <0: 
        heapq.heappush(maxh, -x)
    else:
        if maxh and minh:
            mx = heapq.heappop(maxh)
            mi = heapq.heappop(minh)
            if mx < mi:
                print(-mx)
                heapq.heappush(minh, mi)
            elif mx > mi:
                print(mi)
                heapq.heappush(maxh, mx)
            else: # 같은 경우 더 작은 값
                print(-mx)
                heapq.heappush(minh, mi)
        elif maxh or minh:
            if maxh:
                mx = heapq.heappop(maxh)
                print(-mx)
            else:
                mi = heapq.heappop(minh)
                print(mi)
        else: 
            print(0)
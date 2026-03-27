from collections import deque
import sys
input = sys.stdin.readline 

def bfs(n, k):
    l = min(max(2*n+1,2*k+1), 100001)
    visited = [0]*l
    q = deque()
    q.append(n)
    sec = 1
    visited[n] = sec

    if n == k: 
        return 0

    while q: 
        start = q.popleft()
        sec = visited[start]

        for next in [start-1, start+1, start*2]: # 좌/우/순간 이동
            if 0<= next < l and visited[next] == 0:
                if k == next: 
                    return sec + 1 -1
                visited[next] = sec + 1
                q.append(next)

n, k = map(int, input().split())
result= bfs(n, k)
print(result)
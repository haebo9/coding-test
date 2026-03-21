from collections import deque 
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

def bfs(E,R): 
    global visited, cnt

    # 현재 위치에서 갈수 있는 모든 노드 방문 
    visited[R] = cnt # R : 현재 노드 
    cnt += 1
    
    Q.append(R)
    while Q: 
        u = Q.popleft()
        for v in E[u]: 
            if visited[v] == 0: 
                visited[v] = cnt 
                cnt += 1
                Q.append(v)

N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)] # 노드의 개수+1 만큼 개수의 연결 리스트 

for _ in range(M) : # 무방향
    u, v= map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(N+1): 
    E[i].sort()

visited = [0]*(N+1)
cnt = 1 
Q = deque()

bfs(E,R)
print(*visited[1:], sep='\n')
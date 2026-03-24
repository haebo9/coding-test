import sys
input = sys.stdin.readline 

def dfs(E, V): 
    "깊이 우선 탐색" 
    global visited, result
    visited.add(V)
    result.append(V)

    for x in E[V]: 
        if x not in visited: 
            dfs(E, x)

def bfs(E, V): 
    "너비 우선 탐색"
    global visited, result, q
    visited.add(V)
    result.append(V)
    q.append(V)

    while q: 
        u = q.popleft()
        for v in E[u]: 
            if v not in visited:
                visited.add(v)
                result.append(v)
                q.append(v) # 다음 방문

N, M, V = map(int, input().split())

# edges 관계 연결 리스트
E = [[] for _ in range(N+1)]
for _ in range(M): 
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

# 오름차순 정렬
for e in E: 
    e.sort()

# 노드 방문 DFS
visited = set()
result = list()
dfs(E, V)
print(*result)

# 노드 방문 BFS
from collections import deque
visited = set()
result = list()
q = deque()
bfs(E, V)
print(*result)
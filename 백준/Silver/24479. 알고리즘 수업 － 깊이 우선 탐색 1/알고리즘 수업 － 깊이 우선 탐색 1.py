import sys
input = sys.stdin.readline 
sys.setrecursionlimit(1000000)

# DFS : 깊이 우선 탐색 
def dfs(E, R): 
    global visited, cnt
    visited[R] = cnt 
    cnt += 1

    for x in E[R]: 
        if visited[x] == 0: 
            dfs(E, x) 

N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
for _ in range(M): 
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(N+1): 
    E[i].sort()

visited = [0]*(N+1)
cnt = 1
dfs(E, R) 

print(*visited[1:], sep='\n')
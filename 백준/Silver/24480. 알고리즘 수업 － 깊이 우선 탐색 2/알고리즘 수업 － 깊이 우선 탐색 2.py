import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

def dfs(E, R): 
    global visited, cnt 

    visited[R] = cnt
    for x in E[R]: 
        if visited[x] == 0: 
            cnt += 1
            dfs(E, x)

N, M, R= map(int, input().split())

# edge 정보 연결리스트 구현 
E = [[] for _ in range(N+1)] 
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

# 내부 정렬 (내림차순)
for i in range(1, N+1): 
    E[i].sort(reverse=True)

visited = [0]*(N+1)
cnt = 1
dfs(E, R)
print(*visited[1:], sep='\n') 
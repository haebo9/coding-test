# DFS : 깊이 우선 탐색 
# 정점 = node / 간선 = edge
import sys
input = sys.stdin.readline
# 파이썬은 재귀의 제한이 1000임. 임의적인 늘려주는 것이 필요
sys.setrecursionlimit(200000)

def dfs(V,E,r): # 정점 집합, 간선 집합, 시작 정점
    global visited, cnt
    visited[r] = cnt

    for x in E[r]: # 정점 번호를 오름차순으로 방문 (작은 숫자부터 확인)
        if visited[x] == 0: 
            cnt += 1
            dfs(V,E,x)

n, m, r = map(int, input().strip().split())
V = list(range(1, n+1))

# 인접 행렬을 만들기 (노드 연결 관계) 
E = {v:[] for v in V}
for _ in range(m): 
    i, j = map(int, input().strip().split())
    E[i].append(j)
    E[j].append(i)

# 2. 오름차순 방문을 위해 각 인접 리스트 정렬
for i in range(1, n + 1):
    E[i].sort()

# E = {1: [4, 2], 2: [1, 3, 4], 3: [2, 4], 4: [1, 2, 3], 5: []}
# print(E)

# 간선 관계에 따라 오름차순으로 노드 방문 
visited = [0]*(n+1)
cnt = 1
dfs(V,E,r)
print(*visited[1:], sep='\n')
from collections import deque 
import sys
input = sys.stdin.readline 

def bfs(q, indegree,edges, n, m): 
    "자신을 바라보는 노드가 없는 노드들을 result에 추가하고 관련 노드 들도 연달아 추가" 

    result = []
    while q:
        # 먼저 결과에 들어갈 노드들
        u = q.popleft() 
        result.append(u)

        # 뒤에 나올 노드
        for v in edges[u]: 
            indegree[v] -= 1
            if indegree[v] == 0: 
                q.append(v)
    
    return result 

n, m = map(int, input().split())
indegree = [0]*(n+1) # 자신을 바라보는 노드의 수
edges = [[] for _ in range(n+1)] # u -> v

for _ in range(m):  
    u, v = map(int, input().split())
    indegree[v] += 1
    edges[u].append(v)

q = deque()
for i in range(1, n+1): 
    if indegree[i] == 0: 
        q.append(i)

result = bfs(q, indegree,edges, n, m)
print(*result)
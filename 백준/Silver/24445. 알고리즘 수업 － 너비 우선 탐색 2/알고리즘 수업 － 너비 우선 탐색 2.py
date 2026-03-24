from collections import deque
import sys
input = sys.stdin.readline 

def bfs(e,r): # r은 시작 노드 
    global q, visited, cnt
    # 현재 노드 방문 처리 
    visited[r] = cnt 
    cnt += 1
    # 실행 큐에 추가 
    q.append(r)

    while q: 
        u = q.popleft()
        for v in e[u]: 
            if visited[v] == 0: 
                visited[v] = cnt 
                cnt += 1
                q.append(v)

n, m, r = map(int, input().split())
e = [[] for _ in range(n+1)] # 엣지 집합 : 연결 리스트(각 노드에서 연결된 노드)

for _ in range(m): # 엣지 개수만큼 입력 받음 
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

for i in e:
    i.sort(reverse=True)

visited = [0]*(n+1)
q = deque()
cnt = 1
bfs(e,r)
print(*visited[1:], sep='\n')
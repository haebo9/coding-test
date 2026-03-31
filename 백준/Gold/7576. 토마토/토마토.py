from collections import deque 
import sys
input = sys.stdin.readline 

def bfs(): 
    "토마토가 위치하는 지점(sr, sc)에서 dfs 탐색 시작"
    global visited, zero, result, q

    while q: 
        r,c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우
            nr, nc = r + dr, c + dc 
            # 이동할 곳(nr, nc)가 범위 안에 있고 토마토가 처음에 익지 않은 곳이여야 함
            if 0<= nr < n and 0<= nc < m and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                # dfs 처리의 모든 값은 최적 방문 값임을 보장 
                zero.discard((nr, nc)) # 방문 처리 
                visited[nr][nc] = visited[r][c]+1 
                q.append((nr, nc))
                if result < visited[r][c]+1: 
                    result = visited[r][c]+1

m, n = map(int, input().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
result = 1 # 토마토가 모두 익어 있는 경우

# 처음부터 익은 토마토가 있는 곳에서 출발 ; sr, sc
start = set()
zero = set()
for sr in range(n): 
    for sc in range(m):
        if arr[sr][sc]==1: 
            start.add((sr,sc)) # 시작 집합에 추가
        elif arr[sr][sc]==-1: 
            visited[sr][sc] = -1 # 방문 불가 처리 
        else: 
            zero.add((sr,sc)) # 도착 집합에 추가(0인 값)

# 시작 집합의 위치 부터 탐색 시작 
q = deque()
for sr, sc in start: 
    q.append((sr, sc)) # 동시 출발 처리 
    visited[sr][sc] = 1
bfs()   

# 최댓값 or 익지 않은 토마토 찾기 
if zero: 
    print(-1)
else: 
    print(result-1) # 값 보정 (출발 시간 1 -> 0)
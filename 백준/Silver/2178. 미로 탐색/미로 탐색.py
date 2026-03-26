from collections import deque
import sys
input = sys.stdin.readline 

def bfs(n,m,arr): 
    # 초기값 세팅 
    visited = [[0]*m for _ in range(n)]
    r, c= 0, 0
    visited[r][c] = 1
    q = deque()   
    q.append((0,0))

    while q: 
        # 기준점으로 부터 상하좌우 갈수 있는 곳으로 이동 
        r, c = q.popleft()
        cnt = visited[r][c]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우
            if 0<= r+dr < n and 0<= c+dc < m: 
                if arr[r+dr][c+dc] == 1 and not visited[r+dr][c+dc]: 
                    q.append((r+dr,c+dc))
                    visited[r+dr][c+dc] = cnt + 1 # 이동했으면 이동전 숫자 + 1 기록

    # 먼저 목적지에 도착한 결과가 먼저 기록되게 되어 있음 
    return visited[n-1][m-1]

n,m = map(int, input().split()) 
arr = [[int(i) for i in input().strip()] for _ in range(n)] # N x M 사이즈 배열 

print(bfs(n,m,arr))
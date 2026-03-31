from collections import deque 
import sys
input = sys.stdin.readline 

def solution(m,n,h,arr): 
    visited = [[[0]*m for _ in range(n)] for _ in range(h)]
    q = deque()

    # 최초에 익은 토마토가 존재하는 곳 확인 (없는 곳도)
    for z in range(h): 
        for x in range(n): 
            for y in range(m): 
                if arr[z][x][y] == 1: 
                    q.append((z,x,y))
                    visited[z][x][y] = 1
                elif arr[z][x][y] == -1: 
                    visited[z][x][y] = -1

    # 초기 토마토 위치에서 부터 동시 탐색 시작 
    def bfs(q, visited): 

        while q: 
            z, x, y = q.popleft()
            day = visited[z][x][y]
            
            # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
            for dz, dx, dy in [(-1, 0, 0), (1, 0, 0), (0, 0, -1),(0, 0, 1), (0, -1, 0), (0, 1, 0)]:
                nz, nx, ny = z+dz, x+dx, y+dy
                if 0<= nx < n and 0<= ny < m and 0<= nz < h: 
                    if visited[nz][nx][ny] == 0: 
                        visited[nz][nx][ny] = day + 1
                        q.append((nz, nx, ny))
        
        return visited 

    visited = bfs(q, visited)
    result = 1
    for z in range(h): 
        for x in range(n): 
            for y in range(m): 
                if visited[z][x][y] == 0: 
                    return -1
                elif visited[z][x][y] > result: 
                    result = visited[z][x][y]
    return result-1

m,n,h = map(int, input().split())
arr = [[]*n for _ in range(h)]
for a in arr: 
    for _ in range(n): 
        a.append(list(map(int, input().strip().split())))

print(solution(m,n,h,arr))
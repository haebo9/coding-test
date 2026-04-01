from collections import deque
import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

def bfs(n, m, arr): 
    q = deque([(0,0,0)]) # r: 행, c:열, w:벽 부순적 있는지 여부
    visited = [[[0,0] for _ in range(m)] for _ in range(n)] # [벽 안부숨, 벽 부숨]
    visited[0][0][0] = 1
    visited[0][0][1] = 1

    while q: 
        r, c, w = q.popleft()

        if r == n-1 and c == m-1: 
            return visited[r][c][w]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            nr, nc = r+dr, c+dc
            
            # 기본적인 범위 체크
            if 0<= nr < n and 0<= nc < m: 
                if arr[nr][nc] == '0': # 벽이 아님 
                    # 벽을 부수지 않고 온 경우 / 벽을 부수고 온 경우 
                    if visited[nr][nc][w] == 0: 
                        visited[nr][nc][w] = visited[r][c][w] + 1
                        q.append((nr, nc, w))
                        
                else: # '1' : 벽을 만났음
                    # 오는 길에 벽을 부순적이 없음 -> 이번에 벽을 부심 (w : 0->1)
                    if w==0 and visited[nr][nc][1] == 0:
                        visited[nr][nc][1] = visited[r][c][0] + 1 
                        q.append((nr, nc, 1))

    else: 
        return -1

print(bfs(n, m, arr))
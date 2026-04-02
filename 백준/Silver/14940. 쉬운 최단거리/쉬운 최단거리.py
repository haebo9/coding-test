from collections import deque
# import sys
# input = sys.stdin.readline 

def bfs(i, j, n, m, arr, visited): 

    q = deque([(i, j)])

    while q: 
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            nr, nc = r+dr, c+dc
            if 0<= nr < n and 0<= nc < m: 
                if visited[nr][nc]==-1: 
                    if arr[nr][nc]==1: 
                        visited[nr][nc] = visited[r][c] +1
                        q.append((nr, nc))

def solution(): 
    n, m = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]

    visited = [[-1]*m for _ in range(n)]

    for i in range(n): 
        for j in range(m): 
            if arr[i][j]==2: 
                visited[i][j]= 0
                bfs(i, j, n, m, arr, visited)
            elif arr[i][j]==0: 
                visited[i][j]= 0
    
    return visited
           
for k in solution(): 
    print(*k)
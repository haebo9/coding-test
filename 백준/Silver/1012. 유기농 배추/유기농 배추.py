import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10000)

def dfs(r, c): 
    global grp, visited, arr
    # 현재 위치 방문 처리 
    visited[r][c] = grp

    # 상하 좌우 갈수 있는 곳 이동 
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
        if 0<= r+dr < n and 0<= c+dc < m: 
            if not visited[r+dr][c+dc] and arr[r+dr][c+dc]: 
                dfs(r+dr, c+dc)

t = int(input())
for _ in range(t): 
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    arr = [[0]*m for _ in range(n)]

    # 배추 위치 표시 
    for _ in range(k):
        c, r = map(int, input().split())
        arr[r][c] = 1

    # DFS 이동
    visited = [[0]*m for _ in range(n)]
    grp = 0
    for r in range(n): 
        for c in range(m): 
            if arr[r][c] and not visited[r][c]: 
                grp += 1
                dfs(r, c)
    
    # 최종 그룹 번호 출력 
    print(grp)
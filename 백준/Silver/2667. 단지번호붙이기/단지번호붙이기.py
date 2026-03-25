import sys
input = sys.stdin.readline 
sys.setrecursionlimit(100000)

def dfs(r, c): 
    global n, arr, visited, group, cnt 
    visited[r][c] = group
    cnt[group] += 1

    # 상하 좌우 이동 탐색 
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우
        if (0<= r+dr and r+dr< n) and (0<= c+dc and c+dc< n): 
            if arr[r+dr][c+dc] == 1 and visited[r+dr][c+dc] == 0: 
                dfs(r+dr, c+dc)

# 초기값 설정 
n = int(input())
arr = [[int(i) for i in input().strip()]for _ in range(n)]
visited = [[0]*n for _ in range(n)]
group = 1
cnt = {} 

# 모든 위치에서 탐색 시작(단, 아직 탐색되지 않은 경우)
for r in range(n): 
    for c in range(n): 
        if arr[r][c] == 1 and visited[r][c] == 0: 
            cnt[group] = 0
            dfs(r, c)
            group +=1 

print(len(cnt))
print(*sorted(cnt.values()), sep='\n')
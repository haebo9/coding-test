import sys
sys.setrecursionlimit(1000000)

def solution(land):
    n = len(land)
    m = len(land[0])
    col = [set() for _ in range(m)] # 컬럼별 그룹 종류 저장 
    cnt = {0:0}
    gc = 2 # gc = 1은 방문 가능한 석유 위치 그룹
    
    def dfs(r, c): 
        "모든 석유에 대해 그룹을 지정한다. 인접한 석유는 같은 그룹"
        nonlocal n, m, gc, cnt
        land[r][c] = gc
        
        # 상하좌우 이동 탐색 
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m: 
                if land[nr][nc] ==1: 
                    col[nc].add(gc)
                    cnt[gc] += 1
                    dfs(nr, nc)
        
    for r in range(n): 
        for c in range(m): 
            # 석유가 있는 곳이면서 아직 그룹이 정해지지 않은 곳이면 탐색 시작 
            if land[r][c] == 1: 
                col[c].add(gc)
                cnt[gc] = 1
                dfs(r,c)
                gc += 1 # 그룹 번호 +1
    
    # 컬럼별 획득 가능한 총 석유량 계산
    answer = 0
    for c in col: 
        total = (sum(cnt[i] for i in c))
        if total > answer: 
            answer = total 
            
    return answer
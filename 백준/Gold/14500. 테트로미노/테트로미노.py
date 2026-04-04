import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(n)]

# n, m = 5, 5
# board = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 1, 2, 1]]
# print(board)

def solution(n, m, board):
    result = 0

    def dfs(r, c, total, cnt): 
        nonlocal result, visited

        if cnt == 4: 
            if total > result: 
                result = total
            return 

        for dr, dc in [(0,-1), (0, 1), (-1, 0), (1, 0)]: # 좌 우 상 하
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]: 
                visited[nr][nc] = 1
                dfs(nr, nc, total+board[nr][nc], cnt+1)
                visited[nr][nc] = 0 # 백트랙킹 

    def check(n, m, board, r, c): 
        nonlocal result
        # DFS로 알수 없는 값 : 산(ㅜ) 형 (4가지)
        check = [
            [(0, 0), (0, -1), (0, 1), (1, 0)],  # ㅜ
            [(0, 0), (0, -1), (0, 1), (-1, 0)], # ㅗ
            [(0, 0), (-1, 0), (1, 0), (0, 1)],  # ㅏ
            [(0, 0), (-1, 0), (1, 0), (0, -1)]  # ㅓ
        ]

        # 외부에서 산 형 값 직접 계산
        for ck in check: 
            total = 0
            for dr, dc in ck: 
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m: 
                    total+= board[nr][nc]
                else: 
                    break
            if total > result: 
                result = total

    visited = [[0]*m for _ in range(n)]
    for r in range(n): 
        for c in range(m): 
            # 내부에서 result 갱신 (DFS 로직 탐색) / 현재위치의 값 반영
            visited[r][c] = 1 # 시작 값 방문 처리
            dfs(r, c, total=board[r][c], cnt=1) 
            visited[r][c] = 0 # 백트랙킹 (방문 회수)

            # 내부에서 result 갱신 (ㅗ 모양 직접 탐색)
            check(n, m, board, r, c)
    
    return result

result = solution(n, m, board) 
print(result)
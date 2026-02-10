import sys
input = sys.stdin.readline 

# 브루드포트 알고리즘 
n, m = map(int, input().strip().split())
board = [list(input().strip()) for _ in range(n)]

# 잘못 칠해진 곳 1로 표시
def check_board(board): 
    global n, m

    start = 'W'
    for i in range(n):
        for j in range(0, m, 2): # 짝수
            if board[i][j] == start: 
                board[i][j] = 0
            else: 
                board[i][j] = 1

        for j in range(1, m, 2): # 홀수 
            if board[i][j] == start: 
                board[i][j] = 1
            else: 
                board[i][j] = 0

        start = ('B' if start == 'W' else 'W')
    return board

def cnt_error(_board): 
    result = 64
    for i in range(n-8+1): 
        for j in range(m-8+1):
            
            cnt = 0
            for x in range(i, i+8): 
                for y in range(j, j+8):
                    cnt += _board[x][y]
            
            cnt = min(cnt, 64-cnt)
            if cnt < result: 
                result = cnt

    return result

_board = check_board(board)
result = cnt_error(_board)
print(result)
def solution(board, h, w):
    n = len(board)
    cnt = 0
    for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
        nh, nw = h+dh, w+dw
        if (0<= nh < n and 0<= nw < n) and (board[nh][nw] == board[h][w]): 
            cnt += 1 
    return cnt
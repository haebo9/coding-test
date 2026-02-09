"""
M x N 크기의 보드 -> K x K 로 잘라낸 뒤 다시 칠함. 
맨 위쪽 칸의 색은 흰색(W) or 검은색(B)

return 
K x K 보드를 체스판으로 만들기 위해 다시 칠해야하는 정사각형의 개수의 최솟값

K x K 사이즈로 이동하면서 검사하는 로직이 필요

전략 : 화이트(1), 블랙(0)의 좌표값에 대한 값을 따로 합하여 안맞는 부분의 개수를 구하기 ! 
"""
import sys
input = sys.stdin.readline 

n, m, k = map(int, input().strip().split())
board = [list(input().strip()) for _ in range(n)] # NxM 사이즈 배열

def mapping_board(board, n, m):
    # 먼저 잘못된 곳의 값을 1로 매핑하는 작업이 필요함
    start = board[0][0]
    mapped = [[0]*(m+1) for _ in range(n+1)]
    for i in range(0, n):
        for j in range(0, m, 2): 
            if board[i][j] != start: 
                mapped[i+1][j+1] = 1
        for j in range(1, m, 2): 
            if board[i][j] == start: 
                mapped[i+1][j+1] = 1

        start = ('W' if start == 'B' else 'B')

    # [i][j]의 값은 [i][j] 값에 [i-1][j]와 [i][j-1]의 값을 합한 값
    for i in range(n):
        for j in range(m): 
            mapped[i+1][j+1] = mapped[i+1][j+1] + mapped[i+1][j] + mapped[i][j+1] - mapped[i][j]

    return mapped

def check_range(mapped, n, m, k): 
    # i ~ i+k / j ~ j+k 범위의 값의 합은 [i+k][j+k]의 값에서 좌, 상의 값을 빼고 [i-1][j-1]의 값을 더한 값
    result = n*m
    for i in range(n): 
        for j in range(m): 
            if (i+k <= n) and (j+k <= m):
                # 시작 값이 board[0][0] 인 경우의 수정값 
                temp1 = mapped[i+k][j+k] - mapped[i+k][j] - mapped[i][j+k] + mapped[i][j]
                # 다른 값인 경우의 수정 값 (중요: 시작이 W, B 인 경우를 모두 고려)
                # 패턴이 반대면 앞에서 정답이 여기선 오답이 됨
                temp2 = k**2 - temp1
                temp = min(temp1, temp2)
            if temp < result: 
                result = temp
            
    return result

mapped = mapping_board(board, n, m)
result = check_range(mapped, n, m, k)

print(result)
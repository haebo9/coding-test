def check_q(row, col): 
    """x번째 행의 퀸이 유효한지 확인"""
    global visited_col, visited_rcross, visited_lcross

    if visited_col[col]: # 열 검사(|)
        return False

    if visited_rcross[row+col]: # 우상향 대각선 검사(/)
        return False

    if visited_lcross[row-col+n-1]: # 좌상향 대각선 검사(\)
        return False

    return True
    
def backtrack(row=0): # 0번째 행부터 시작
    """
    i == j : 같은 행
    array[i] == array[j] : 같은 열 

    (i + array[i]) == (j + array[j]) : 같은 대각선(우상향) 
    (i - array[i] + n -1) == (j - array[j] + n -1) : 같은 대각선(좌상향) + 양수 보정
    * n-1 양수 보정: 두 값의 가능한 차의 최대인 n에 인덱스값인점을 보정하여 -1 처리 한것 

    우상향 : (4, 1) (3, 2) (2, 3), (1, 4) -> 합이 동일
    좌상향 ; (1, 1) (2, 2) (3, 3) ...  -> 차가 동일

    놓을 수 있는 곳이 없으면 돌아와서 이전에 놓은 곳을 방문 처리 하고 다른 곳 탐색
    퀸은 가장 위의 행부터 하나씩 이동 (= 같은 행에 퀸이 두번 들어갈 일 없음) 
    """
    global array, result, visited_col, visited_rcross, visited_lcross

    if row == n: 
        result += 1
        return 

    for col in range(n): # 한 행에 퀸을 어떤 열에 놓을 지 선택
        if check_q(row, col): 

            array[row] = col
            visited_col[col] =True
            visited_rcross[row+col] = True
            visited_lcross[row-col+n-1] = True

            backtrack(row+1) # 다음 행으로 이동하여 반복

            visited_col[col] = False
            visited_rcross[row+col] = False
            visited_lcross[row-col+n-1] = False

            # 조건이 맞지 않을 떈 다음 행으로 넘어가지 않고 다음 반복문 실행

n = int(input())
array = [0]*(n) # i번째 값은 array[i][value] 위치에 퀸이 있다는 의미 # 1차원으로 표현
result = 0

visited_col = [False]*(n) # col 
visited_rcross = [False]*(2*n) # row + col 
visited_lcross = [False]*(2*n) # row - col + n -1

backtrack()
print(result)
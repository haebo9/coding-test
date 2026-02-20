def is_possible(row, col, num): 
    """ 특정 위치에 num 값이 가능한지를 확인하는 함수 """ 
    global array, visited

    # 분단 확인
    ch_row = row // 3
    ch_col = col // 3

    # 같은 분단에 있는지
    if num in visited[ch_row][ch_col]:
        return False
    
    # 같은 열에 있는지 
    for i in range(9): 
        if num == array[i][col]: 
            return False

    return True

def backtrack(index=0): 
    """
    1. 0의 위치별로 이동하면서 가능한 숫자를 확인한다. 
    2. 해당 숫자가 가능할 때, 입력하고 다음 0으로 이동한다. 
    3. 해당 0에 어떤 숫자도 채울 수 없는 경우, 이전 노드를 0으로 초기화 한뒤 다음 숫자를 시도한다. 
    """
    global array, zeros, one_to_nine

    if index == len(zeros) : # 모든 0의 위치를 채웠을 때
        return True
    
    row, col = zeros[index] # 특정 index 에서 0 이 위치한 좌표
    target = one_to_nine - set(array[row]) # 사용 가능한 숫자만 사용(행 검사 대체)

    for num in target: # 들어가는 값
        if is_possible(row, col, num): 
            # 가능한 숫자로 채움
            array[row][col] = num

            # visited 갱신
            ch_row = row // 3
            ch_col = col // 3
            visited[ch_row][ch_col].add(num)

            # 다음 0의 위치로 이동
            if backtrack(index+1): 
                return True

            # return 되지 않고 돌아왔을 때, 이전값 초기화 하고 다음 숫자 시도 
            else: 
                array[row][col] = 0
                visited[ch_row][ch_col].remove(num)

    # 모든 숫자에 대해 시도했는데 반환되지 않은 경우 
    return False

def f_visited(array): 
    visited = []

    for r in range(0, 9, 3): 
        gr = []
        for c in range(0, 9, 3): 
            temp = set()
            for i in range(r, r+3): 
                for j in range(c, c+3):
                    temp.add(array[i][j]) 
            gr.append(temp)
        visited.append(gr)
    
    return visited

import sys
input = sys.stdin.readline 

array = [list(map(int, input().strip().split())) for _ in range(9)]
# array = [[0, 3, 5, 4, 6, 9, 2, 7, 8], [7, 8, 2, 1, 0, 5, 6, 0, 9], [0, 6, 0, 2, 7, 8, 1, 3, 5], [3, 2, 1, 0, 4, 6, 8, 9, 7], [8, 0, 4, 9, 1, 3, 5, 0, 6], [5, 9, 6, 8, 2, 0, 4, 1, 3], [9, 1, 7, 6, 5, 2, 0, 8, 0], [6, 0, 3, 7, 0, 1, 9, 5, 2], [2, 5, 8, 3, 9, 4, 7, 6, 0]]
zeros = [(r, c) for r in range(9) for c in range(9) if array[r][c]==0]
one_to_nine = set(range(1, 10))

# 같은 분단에 있는지
visited = f_visited(array)

backtrack()

for a in array: 
    print(*a)
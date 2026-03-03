# 분할 정복 

def paper_cut(x, y, size): 
    "start부터 end까지의 영역에 같은 색일때의 카운트를 구하는 함수"
    global blue, white

    color = lst[x][y]
    
    # 영역 안에 하나라도 다른 색 발견
    for i in range(x, x+size): 
        for j in range(y, y+size): 
            if lst[i][j] != color:
                new_size = size//2 
                paper_cut(x,y, new_size) # 1
                paper_cut(x,y+new_size, new_size) # 2
                paper_cut(x+new_size, y, new_size) # 3
                paper_cut(x+new_size,y+new_size, new_size) # 4
                return 

    # return 되지 않고 옴 = 모두 같은 색깔 
    if color == 0: 
        white += 1
    else: 
        blue += 1

import sys
input = sys.stdin.readline 

n = int(input())
lst = [list(map(int, input().strip().split())) for _ in range(n)]
# lst =[[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
 
blue = 0
white = 0

paper_cut(0, 0, n)
print(white)
print(blue)
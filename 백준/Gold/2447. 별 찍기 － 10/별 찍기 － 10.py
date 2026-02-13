def recursive(n, x, y):
    """ 가운데가 비워진 정사각형을 반환 """
    if n == 1: 
        return 

    size = n // 3

    for i in range(3): 
        for j in range(3): 
            # 9개의 구역 중에 가운데 구역을 공백으로 제거 
            if i == 1 and j == 1: 
                for row in range(x + size, x + 2*size):
                    for col in range(y + size, y + 2*size): 
                        square[row][col] = ' '
            # 나머지 구역은 재귀적 실행 
            else: 
                recursive(size, x + i*size , y + j*size)

# NxN의 정사각형을 9등분 된 사각형의 합으로 나타낼 수 있어야 함. 
# 범위로 나타내야함. 0~N-1
import sys
input = sys.stdin.readline 

n = int(input())
square = [['*']*n for _ in range(n)]

recursive(n, 0, 0)
for i in square:
    print(*i, sep='')
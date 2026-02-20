# n 개의 정사각형이 한 줄에 있다는 것은 n개의 층으로 되어 있다는 말. 
# n개의 층일때 상단은 변이 1개, 하단은 변이 n개, 옆면은 n*2개, 잘린 틈은 n-1개 

import sys 
input = sys.stdin.readline 

n = int(input())
result = 1 + n + n*2 + (n-1)
print(result) 
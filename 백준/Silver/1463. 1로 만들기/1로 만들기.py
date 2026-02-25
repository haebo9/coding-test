def backtrack(n, cnt): 
    " 조기 종료 조건을 가진 반복문 " 
    global result
    if n == 1: 
        result = cnt 
        return 

    if cnt >= result: 
        return 

    if n % 3 == 0: 
        backtrack(n//3, cnt+1)
    if n % 2 == 0: 
        backtrack(n//2, cnt+1)
    if n-1 > 0:
        backtrack(n-1, cnt+1)

import sys
input = sys.stdin.readline 

n = int(input())
result = float('inf')

backtrack(n, cnt=0)
print(result)
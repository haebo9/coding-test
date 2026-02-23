# 삼각형의 절대 조건 : 두 변의 합이 가장 긴 한 변의 길이보다 커야 한다. 

def triangle(a,b,c): 
    if a < b+c: 
        return a+b+c
    else: 
        return triangle(a-1, b, c)

import sys
input = sys.stdin.readline 

a,b,c = sorted(map(int, input().strip().split()), reverse=True) 
print(triangle(a,b,c))
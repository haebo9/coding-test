# 최대 공약수 ; 유클리드 정리 사용
def uclid(a,b): 
    while b: 
        a, b = b, a%b
    print(a)
    return a

# 최소 공배수 (lcd)
def min_squre(a,b): 
    return (a*b)//uclid(a,b)

import sys
input = sys.stdin.readline 

a, b= map(int, input().strip().split())
print(min_squre(a,b))
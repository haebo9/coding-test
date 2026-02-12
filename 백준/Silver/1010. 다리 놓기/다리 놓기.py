from math import factorial as fac
import sys
input = sys.stdin.readline

def bridge(n, m):
    # 큰 수에서 작은 수의 개수만큼 뽑는 경우의 수 (중복 없음)
    # 무조건 right가 더 크다고 가정
    if n <= m : 
        s = n
        b = m
    else: 
        s = m
        b = n

    result = fac(b) // (fac(s)*fac(b-s))
    return result

for _ in range(int(input())): 
    n, m = map(int, input().strip().split())
    print(bridge(n,m))
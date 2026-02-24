import sys
input = sys.stdin.readline 

import math 

def a_num(a): 
    """ greedy : 총감독관 무조건 1명, 나머지 부감독관 필요수 계산"""
    global  b, c
    # 총 감독관 1명
    total = 1 + math.ceil(max(0, a - b) / c) 

    return total

n = int(input())
a_lst = list(map(int, input().strip().split()))
b, c = map(int, input().strip().split())

result = 0
for a in a_lst: 
    result += a_num(a)

print(result) 
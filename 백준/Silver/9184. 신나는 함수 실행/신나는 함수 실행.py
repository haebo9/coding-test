# 메모이제이션(캐싱)
def w(a,b,c):
    global cache

    # 캐싱되어 있으면 가져다 씀
    if (a,b,c) in cache:
        return cache[(a,b,c)]

    # 없으면 계산해서 캐싱
    else:
        if a <= 0 or b <= 0 or c <= 0:
            cache[(a,b,c)] = 1
            
        elif a > 20 or b > 20 or c > 20:
            cache[(a,b,c)] = w(20, 20, 20)

        elif a < b and b < c:
            cache[(a,b,c)] = w(a,b,c-1) + w(a,b-1, c-1) - w(a, b-1, c)

        else:
            cache[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        
        return cache[(a,b,c)]

import sys
input = sys.stdin.readline 

cache = {}

while True: 
    a,b,c = map(int, input().strip().split())

    if a==-1 and b==-1 and c==-1: 
        break
    else: 
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
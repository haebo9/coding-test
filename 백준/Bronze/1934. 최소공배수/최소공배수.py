def min_cross(a, b): 
    if b % a == 0: 
        return b
    
    # 두 수를 동시에 나눌 수 있는 수가 있으면 작은 수만 나눔 
    i = 2
    temp_b = b
    while i <= a: 
        while a % i == 0 and temp_b % i == 0: 
                a //= i
                temp_b //= i
        i += 1

    return a*b

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d1, d2= map(int, input().strip().split())  
    a, b= min(d1, d2), max(d1, d2) 
    print(min_cross(a,b))
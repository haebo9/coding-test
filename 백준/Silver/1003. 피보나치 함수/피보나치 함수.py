def result(n):
    a,b = 1, 0
    if n > 0: 
        a, b = 0, 1
        for _ in range(0, n-1): 
            a, b = b, a+b
    print(a,b)

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result(n)
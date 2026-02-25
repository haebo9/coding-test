def all_search(n): 
    global cnt
    if n == 0: 
        cnt += 1
        return 

    if n >= 1: 
        all_search(n-1)
    if n >= 2: 
        all_search(n-2)
    if n >= 3: 
        all_search(n-3)

import sys
input = sys.stdin.readline 

for _ in range(int(input())):
    cnt = 0
    n = int(input())

    all_search(n)
    print(cnt)
def ox_check(ox):
    total = 0
    score = 1
    for i in ox: 
        if i == 'O': 
            total += score
            score += 1
        else: 
            score = 1
    return total

import sys 
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ox = input().strip()
    print(ox_check(ox))
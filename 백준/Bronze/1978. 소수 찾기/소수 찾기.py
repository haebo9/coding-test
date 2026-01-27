def decimal(num):
    cnt = 0
    for i in range(1, num//2+1):
        if num % i ==0:
            cnt += 1
    if cnt == 1: 
        return True
    else: 
        return False

import sys
input = sys.stdin.readline
n = int(input().strip())
nums = map(int, input().strip().split())
result = 0

for i in nums: 
    if decimal(i): 
        result += 1

print(result)
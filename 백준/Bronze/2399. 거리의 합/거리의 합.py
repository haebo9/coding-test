import sys
input = sys.stdin.readline 

n = int(input())
nums = sorted(map(int, input().strip().split()))

def solution(n, nums): 
    result = 0
    if n == 1: 
        return 0

    for i in range(n): 
        for j in range(i+1, n): 
            result += nums[j] - nums[i]

    return result*2

print(solution(n, nums))
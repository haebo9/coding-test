import sys
input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().strip().split()))

def solution(n, arr): 
    "dp의 모든 값은 자신의 좌측에서 수열 값이 작은 것 중에서 누적된 부분 수열 길이가 가장 긴 것에 1을 더한 값이다."
    result = 0
    dp = [0]*n
    for i in range(0, n): # 1~i
        for j in range(0, i): # 0~i-1
            if arr[j] < arr[i] and dp[i] < dp[j]: 
                dp[i] = dp[j]
        dp[i] += 1
        if dp[i] > result: 
            result = dp[i]
    
    return result

print(solution(n, arr))
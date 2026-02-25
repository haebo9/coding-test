# DP 
import sys
input = sys.stdin.readline 

n = int(input())
stair = [int(input()) for _ in range(n)]

# i번째 계단에서의 최댓값
dp = [0]*(n)

def move_dp(n):
    """
    i번째 계단에 도달했을때의 최댓값을 구하는 함수 

    1. 직전 계단에서 올라온 경우 : dp[i-3] + stair[i-1] + stair[i]
    2. 두 칸 아래서 점프해온 경우 : dp[i-2] + stair[i]
    """ 
    if n >= 1:
        dp[0] = stair[0]
    if n >= 2: 
        dp[1] = stair[0] + stair[1]
    if n >= 3: 
        dp[2] = max(stair[0], stair[1]) + stair[2]
    if n >= 4: 
        for i in range(3, n): 
            temp1 = dp[i-2] + stair[i] # 직전 계단에서
            temp2 = dp[i-3] + stair[i-1] + stair[i] # 두칸 아래서
            dp[i] = max(temp1, temp2) 

move_dp(n)
print(dp[-1])
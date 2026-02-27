# 계단 수 = 모든 자리의 차가 1 (0으로 시작하면 안됨)
# dp : 길이가 n인 계단 수의 개수는 이전 수를 기반으로 계산 가능 

def stair_dp(): 
    """
    이전 수가 0인 경우 : 다음 수는 반드시 1
    이전 수가 9인 경우 : 다음 수는 반드시 8
    이전 수가 1~8인 경우 : 다음 수는 -1 또는 +1 한 수
    """
    # dp[i][j] : 길이가 i이고, 마지막 숫자가 j인 계단의 개수
    dp = [[0]*10 for _ in range(n+1)]

    # dp의 첫번쨰 값은 1 (개별 수를 1개 넣는 방법)
    for j in range(1, 9+1): 
        dp[1][j] = 1

    # 두번째 자리 부터 N번째 자리까지의 계단의 수 계산
    for i in range(2, n+1): # i : 길이
        for j in range(10): # j : 마지막 숫자
            if j == 0: 
                dp[i][j] = dp[i-1][1] % mod
            elif j == 9: 
                dp[i][j] = dp[i-1][8] % mod
            else: 
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
    return sum(dp[n]) % mod

import sys
input = sys.stdin.readline 

n = int(input())
mod = 10**9
print(stair_dp())
def solution(n):
    dp = [0]*(n)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n): 
        # i번째에 새로 타입을 넣는 경우 = dp[i-1]
        # i-1 ~ i 자리에 가로 타입을 넣는 경우 = dp[i-2]
        dp[i] = (dp[i-1] + dp[i-2]) %1_000_000_007 

    return dp[-1] %1_000_000_007 
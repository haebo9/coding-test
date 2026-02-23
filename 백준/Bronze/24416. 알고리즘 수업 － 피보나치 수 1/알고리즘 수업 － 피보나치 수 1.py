def fib_recur(n): 
    global cnt1
    if n ==1 or n == 2: 
        # cnt1 += 1
        return 1
    else: 
        return fib_recur(n-1) + fib_recur(n-2)

def fib_dp(n): 
    global cnt2
    dp = [1, 1]
    for i in range(2, n):
        dp.append(dp[-1] + dp[-2])
    cnt2 = len(dp)-2 # 초기 2개 값 제외
    return dp[n-1]

import sys 
input = sys.stdin.readline 

n = int(input())

cnt1 = fib_dp(n)
cnt2 = 0
fib_dp(n)

print(cnt1)
print(cnt2)
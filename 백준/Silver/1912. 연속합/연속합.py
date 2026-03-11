# 현재의 값을 선택했을 때, 좌측의 값 중 얻을 수 있는 가장 큰 값을 선택 
def dp(): 

    dp = [0]*n 

    for i in range(n): 
        # 자기 자신을 선택하는 것과 이전 값을 포함하는 것 중 이득이 되는 것을 선택)
        dp[i] = max(arr[i], arr[i] + dp[i-1]) 
    
    return max(dp)

import sys
input = sys.stdin.readline 

n = int(input()) 
arr = list(map(int, input().strip().split()))
print(dp())
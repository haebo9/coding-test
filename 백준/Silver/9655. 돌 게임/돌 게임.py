# 돌이 1개 있을 때 부터 N개 있을 때 까지의 이기는 사람을 입력 
# 마지막 돌을 가져가는 사람이 게임을 이김

# 상근이가 이기는 경우 1: 돌이 1개 남아서 1개를 선택 
# 상근이가 이기는 경우 2: 돌이 3개 남아서 3개를 선택 

import sys
input = sys.stdin.readline 

n = int(input())

def dp(): 
    # 전체 K(=idx)개의 돌에서 마지막 선택하는 돌의 개수
    dp = [-1, True, False, True] # 0-3

    if n > 3: 
        for i in range(4, n+1): 
            if dp[i-3] or dp[i-1]: # 개수 1 or 3개 전에 자신이 이긴 경우(True) 
                dp.append(False)
            else: 
                dp.append(True)
    
    return dp[n]
    
print('SK' if dp() else 'CY')
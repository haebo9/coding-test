# 0과 1이 쓰여있음 -> 00과 1만 존재
# 00만 잘 배치하면 나머지 자리에는 1을 넣으면 됨. 
# n=2 : 00 11
# n=3 : 100 111 001 
# n=4 : 1100 1111 1001 0011 0000
# n=5 : 11100 11111 11001 10011 10000 00111 00001 00100
# n칸이 있을떄 00은 n-1개의 자리를 가짐 

from collections import deque

def tile_dp(n):
    """ 
    n의 작은 단위에서부터의 값을 늘려가며 계산 
    n번째 맨 앞에 추가되는 값은 0또는 1
        0 이 오는 경우 반드시 n-1번째 값중에 0으로 시작해야함 -> n-2번째 값
        1 이 오는 경우 모든 경우 가능 -> n-1번쨰 값
    n = 1: 1
    n = 2: 00 11
    """
    # (a, b) : a는 맨앞이 0, b는 맨앞이 1 이 오는 가지수
    dp = deque([0, 1, 2])

    # n은 1이상의 값이다. (n = 1,2 일때의 처리도 필요)
    if n == 1 or n==2: 
        return dp[n]

    for i in range(3, n+1): 
        # print(dp)
        # 다음 값 추가
        dp.append((dp[-2]+dp[-1])%15746)
        dp.popleft()
    
    return dp[-1]

import sys
input = sys.stdin.readline 

n = int(input())
print(tile_dp(n))
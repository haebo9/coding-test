# 가장 많은 포도주를 먹도록 하는 프로그램 
# 연속 3잔을 모두 마실 수 없음. 
# 백트랙킹, DP

def largest_wine(n, array): 
    """ 
    각 포도주를 마실지 말지 판단할 수만 있으면 됨
    
    6, 10, 13, 9, 8, 1 에서 최대량을 구하는 법 
    - K번쨰에서의 최댓값 : max(k + k-1에서의 최댓값, k + k-2에서의 최댓값, 자신을 뺀 최댓값)
        - K-1에서의 최댓값 : K, K-1이 포함되기에 = K-3까지의 최댓값 + K + K-1
        - k-1의 최댓값(자신 제외) : k-1 까지의 최댓값
        - K-2에서의 최댓값 : K-1은 없음. K + K-2 까지의 최댓값 
    
    RETURN
    N에서의 최댓값을 출력 
    """
    # n이 3미만 일때
    if n < 3:
        if n == 1: 
            return array[0]
        elif n == 2: 
            return array[0]+array[1]
        else: 
            return sum(array[:3])-min(array[:3])

    # n이 3이상 일때 
    else:
        dp = [array[0], array[0]+array[1], sum(array[:3])-min(array[:3])]

        for i in range(3, n): 
            temp1 = dp[i-3] + array[i] + array[i-1] 
            temp2 = dp[i-2] + array[i]
            temp3 = dp[i-1]
            dp.append(max(temp1, temp2, temp3))
    # print(dp)
    return dp[-1]

import sys
input = sys.stdin.readline 

n = int(input())
array = [int(input()) for _ in range(n)]
# array = [6, 10, 13, 9, 8, 1]
# print(array)
print(largest_wine(n, array))
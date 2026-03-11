# DP
# 이전의 합 + 자기자신 vs 자기자신 
# 이전의 합을 가져갈지 말지를 선택
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().strip().split()))

dp = [0]*(n) # i번째 값을 포함했을떄 합의 최댓값
dp[0] = array[0]

for i in range(1, n): # index
    dp[i] = max(dp[i-1]+array[i], array[i])

print(max(dp))
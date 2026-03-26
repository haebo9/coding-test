import sys
input = sys.stdin.readline 

n = int(input())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]
dp = [0,0,0]

# arr(집)을 하나씩 순회하며 dp 최솟값 갱신 
for i in range(n): 
    r,g,b = arr[i]
    dp[0],dp[1],dp[2] = r + min(dp[1], dp[2]), g + min(dp[0], dp[2]), b + min(dp[0], dp[1])

print(min(dp))
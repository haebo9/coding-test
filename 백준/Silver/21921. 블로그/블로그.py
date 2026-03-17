# curr(idx) 값을 반드시 포함 = curr값 + curr-1값 - curr-x의 값 
import sys
input = sys.stdin.readline 

n, x = map(int, input().strip().split())
visited = list(map(int, input().strip().split()))
dp = []

for i in range(n): 
    temp = visited[i]
    if i > 0: 
        temp += dp[i-1]
    if i-x >= 0: 
        temp -= visited[i-x]
    dp.append(temp)

from collections import Counter
cnt = Counter(dp)
max_cnt = max(cnt)

if max_cnt: 
    print(max_cnt)
    print(cnt[max_cnt])
else: 
    print('SAD')
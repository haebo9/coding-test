import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[2], x[3]), reverse=True)

rk = [0]*(n+1)
_, g, s, b = arr[0]
curr_rk = 1

for i in range(n): 
    t = arr[i] 
    # 기준값과 같으면 공동 순위 / 기준값보다 작으면 정상 순위(i+1) 
    if g == t[1] and s == t[2] and b == t[3]: 
        rk[t[0]] = curr_rk
    else: 
        rk[t[0]] = i+1
        curr_rk = i+1
        _, g, s, b = arr[i]

print(rk[k])
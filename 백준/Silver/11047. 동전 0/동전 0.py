n, k = map(int, input().strip().split())
coins = [int(input()) for i in range(n)][::-1] 
cnt_sum = 0

for c in coins: 
    if k >= c: 
        cnt, k = k//c, k%c
        cnt_sum += cnt

print(cnt_sum)
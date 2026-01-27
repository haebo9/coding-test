import copy 
n, k = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    if n % i == 0: 
        cnt += 1
    if cnt == copy.copy(k): 
        print(i)
        break
else: 
    print(0)
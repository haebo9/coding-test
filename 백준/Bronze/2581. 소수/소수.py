def decimal(n, m):
    deci = []
    for t in range(n, m+1):
        cnt = 0
        for i in range(1, m//2+1):
            if i >= t:
                break 
            if t % i == 0: 
                cnt += 1
        if cnt == 1 :
            deci.append(t)
    
    if deci: 
        return deci
    else: 
        return 

import sys
input = sys.stdin.readline

m = int(input().strip())
n = int(input().strip())

deci = decimal(m, n)
if deci: 
    print(sum(deci))
    print(deci[0])
else: 
    print(-1)
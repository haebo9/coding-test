def decimal(m, n): 
    result = []
    target = m
    if target <= 2: 
        result.append(2)
        target = 3

    while target <= n: 
        if target % 2 != 0: 
            for i in range(3, int(n**0.5)+1, 2): 
                if target != i and target % i == 0: 
                    break
            else: 
                result.append(target)

        target += 1
    return result 

import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
print(*decimal(m, n), sep='\n')
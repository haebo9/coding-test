def decimal(n:int)->int:
    if n == 0: return 2
    elif n == 1: return 2
    elif n == 2: return 2
    elif n == 3: return 3
    elif n == 4: return 5
    elif n == 5: return 5
    elif n == 6: return 7
    elif n == 7: return 7
    else: 
        target = n
        while True: 
            for i in range(2, int(target**0.5)+1 ):
                if target != i and target % i == 0 : 
                    target += 1
                    break 
            else: 
                return target

import sys
input = sys.stdin.readline 

for _ in range(int(input())):
    n = int(input())
    print(decimal(n))
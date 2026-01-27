import copy
import sys
input = sys.stdin.readline

n= int(input().strip())
if n == 1: 
    deci_curr = None
else:
    deci = iter(range(2, int(n**0.5)+2))
    deci_curr = next(deci)

while deci_curr is not None and n > 1:      
    if n % deci_curr == 0: 
        print(deci_curr)
        n //= deci_curr
        continue
    else: 
        deci_curr = next(deci, None)

if n > 1: 
    print(n)
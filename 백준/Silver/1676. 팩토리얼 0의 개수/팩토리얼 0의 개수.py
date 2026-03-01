import math 
import sys
input = sys.stdin.readline 

num = str(math.factorial(int(input().strip())))
n = list(num[::-1])

cnt = 0
for i in n: 
    if i == '0': 
        cnt +=1
    else: 
        print(cnt) 
        break

else: 
    print(cnt)
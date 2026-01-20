# 0.25=25센트, 0.10=10센트, 0.05=5센트, 0.01=1센트
def to_coin(num): # num=cent값 (1달러 = 100센트) 
    temp = []
    temp.append(num//25) ; num = num%25
    temp.append(num//10) ; num = num%10
    temp.append(num//5) ; num = num%5
    temp.append(num//1) ; num = num%1
    return temp 

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    c = int(input())
    print(*to_coin(c))
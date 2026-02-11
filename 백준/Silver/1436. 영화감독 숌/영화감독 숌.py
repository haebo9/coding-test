"""
종말의 수 : 연속된 6이 적어도 3개 이상 들어간 수 

666 1666 2666 3666 ... 9666 : 10개 
10666 11666 12666 13666 ... 19666 : 10개 

"""
import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
for i in range(666, 100000000):
    if '666' in str(i):
        cnt += 1
    if cnt == n: 
        print(i)
        break
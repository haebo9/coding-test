from collections import Counter
import sys
input = sys.stdin.readline

# 1은 최대한 앞의 것을 지우고, 0은 최대한 뒤의 것을 지우면 될듯

s = input().strip()

# 지워야 하는 개수를 확인
c = Counter(s)
t0 = c['0']//2
t1 = c['1']//2

result = list(s)

for i in range(c['0'] + c['1']): 
    if s[i] == '1' and t1: 
        result[i] = ''
        t1 -= 1
    if s[-1-i] == '0' and t0: 
        result[-1-i] = ''
        t0 -= 1

print(''.join(result))
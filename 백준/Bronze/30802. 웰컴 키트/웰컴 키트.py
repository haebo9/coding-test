import sys
input = sys.stdin.readline 

import math 

n = int(input())
tshirts = list(map(int, input().strip().split()))
t, p = map(int, input().strip().split())

# 티셔츠는 t장을 한 묶음으로 함. ; 5의 몫 - 반올림
# 펜은 남거나 부족하면 안됨 ; p자루씩 or 1자루씩 ; 7의 몫과 나머지

tshirts = [math.ceil(i/t) for i in tshirts]
pen =[n//p, n%p]
print(sum(tshirts))
print(*pen)
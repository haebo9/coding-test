import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))
comb = combinations(cards, 3)

result = 0
for i in comb: 
    temp = sum(i)
    if temp <= m and temp >= result:
        result = temp 

print(result)
import sys
input = sys.stdin.readline 

from itertools import combinations

n, m = map(int, input().strip().split())

for i in combinations(range(1, n+1), m):
    print(*i)
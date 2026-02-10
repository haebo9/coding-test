import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

comb = sorted([sum(i) for i in combinations(cards, 3) if sum(i) <= m])
print(comb[-1])
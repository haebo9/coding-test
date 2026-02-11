from itertools import permutations

n,m = map(int, input().strip().split())
lst = range(1, n+1)

for i in permutations(lst, m):
    print(*i)
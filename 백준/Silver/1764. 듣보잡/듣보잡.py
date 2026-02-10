import sys
input = sys.stdin.readline 

n,m = map(int, input().strip().split())

no_hear = set([input().strip() for _ in range(n)])
no_see = set([input().strip() for _ in range(m)])

result = no_hear & no_see
print(len(result))
print(*sorted(result), sep='\n')
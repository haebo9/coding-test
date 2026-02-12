import sys
input = sys.stdin.readline 

from itertools import permutations

n = int(input())
lst = list(range(1,n+1))

print(len(list(permutations(lst,2))))
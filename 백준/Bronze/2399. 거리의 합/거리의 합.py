from itertools import combinations
import sys
input = sys.stdin.readline 

n = int(input())
lst = list(map(int, input().strip().split()))
sorted_lst = sorted(lst)

result = [0]*n
for i in range(n): 
    tp = sorted_lst[i]
    result[i] = 2* (tp*(i) - tp*(n-i-1))

print(sum(result))
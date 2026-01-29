import sys
input = sys.stdin.readline 

n = int(input())

lst = []
for _ in range(n): 
    x, y = map(int, input().strip().split())
    lst.append((y, x))

lst = sorted(lst)

for n in lst:
    print(n[1], n[0])
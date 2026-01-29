import sys
input = sys.stdin.readline 

lst = []
for i in range(int(input())):
    a, b = map(int, input().strip().split())
    lst.append((a,b))

sorted_lst = sorted(lst, reverse=True)
while sorted_lst: 
    print(*sorted_lst.pop())
import sys
input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
    age, name = input().strip().split()
    lst.append( (int(age), i, name) )

sorted_lst = sorted(lst)
for i in sorted_lst: 
    print(i[0], i[2])
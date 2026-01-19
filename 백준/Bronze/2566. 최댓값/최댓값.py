import sys

lst = []

for _ in range(9):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    lst.append(temp)

max_num = 0
r, c = 0, 0 
for i in range(9):
    for j in range(9):
        if lst[i][j] > max_num:
            max_num = lst[i][j]
            r, c = i, j

print(max_num)
print(r+1, c+1)
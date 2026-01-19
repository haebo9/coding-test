field = [[0]*101 for _ in range(101)]

def check_field(x, y): 
    for i in range(x, x+10):
        for j in range(y, y+10):
            field[i][j] = 1
import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    x, y= map(int, sys.stdin.readline().strip().split())
    check_field(x, y)

print(sum([sum(i) for i in field]))
import sys
input = sys.stdin.readline
n = int(input())

result = -1
for i in range(n//3 + 3): 
    for j in range(n//5 + 5): 
        if ( 3*i + 5*j == n ) and ((result == -1) or (i + j < result)):
            result = i + j

print(result)
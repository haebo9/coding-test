import sys
input = sys.stdin.readline 

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
target = 0 
result = [] 
for i in range(1, n+1): 
    stack.append(i)
    result.append('+')
    while stack and stack[-1] == arr[target]: 
        stack.pop()
        result.append('-')
        target += 1

if stack: 
    print('NO')
else: 
    print(*result, sep='\n') 
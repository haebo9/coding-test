import sys
input = sys.stdin.readline 

def backtrack(result): 
    if len(result)==m: 
        print(*result)
        return 

    for i in range(1, n+1): 
        backtrack(result+[i]) 

n, m = map(int, input().split())
result = []
backtrack(result)
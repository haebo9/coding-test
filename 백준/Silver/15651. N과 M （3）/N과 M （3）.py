def backtrack(): 
    if len(arr) >= m: 
        print(*arr)
        return 

    for i in range(1, n+1): 
        visited[i] = True
        arr.append(i)

        backtrack()

        arr.pop()
        visited[i] = False

import sys
input = sys.stdin.readline 

n, m = map(int, input().strip().split())
arr = []
visited = [False]*(n+1)
backtrack()
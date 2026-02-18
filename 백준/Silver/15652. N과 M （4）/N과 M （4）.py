import sys
input = sys.stdin.readline 

n, m = map(int, input().strip().split())
array = [] 
visited = [False]*(n+1) 

def backtrack(): 
    if len(array) >= m: 
        print(*array)
        return

    for i in range(1, n+1): 
        if array and i < array[-1]: 
            continue

        array.append(i)
        backtrack()
        array.pop()

backtrack()
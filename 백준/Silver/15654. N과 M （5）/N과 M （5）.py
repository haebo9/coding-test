import sys
input = sys.stdin.readline 

def backtrack(result, chk): 
    if len(result)==m: 
        print(*result)
        return 

    for i in range(n): 
        if arr[i] not in chk: 
            backtrack(result +[arr[i]], chk|set([arr[i]]))

n, m = map(int, input().split())
arr = sorted(map(int, input().strip().split())) # n개의 수열 

backtrack(result=[], chk=set())
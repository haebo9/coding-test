import sys
input = sys.stdin.readline 

# 가능한 모든 경로로 이동하면서 누적값 확인 
def backtrack(r, c, path, total): 
    global n, m, arr, result
    if r == n: 
        if total < result : 
            result = total 
        return 
    
    for p in [1,2,3]: # 움직일 수 있는 방향 
        if p != path: 
            if p ==1 and c-1 >= 0: 
                backtrack(r+1, c-1, p, total+arr[r][c])
            elif p ==2: 
                backtrack(r+1, c, p, total+arr[r][c])
            elif p == 3 and c+1 < m: 
                backtrack(r+1, c+1, p, total+arr[r][c])

# 입력 값
n, m = map(int, input().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

# 모든 위치에서 출발 고려
result = float('inf')
for c in range(m): 
    backtrack(r=0, c=c, path=0, total=0)
print(result)
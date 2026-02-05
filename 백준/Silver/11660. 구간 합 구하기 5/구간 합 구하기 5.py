import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
n2list = [[0]*(n+1)] + [[0]+ list(map(int, input().strip().split())) for i in range(n)]


"""
# (x1, y1)에서 (x1, y2)의 합 = (x1, y1) 까지의 합 - 좌측 패딩 - 위쪽 패딩 + 패딩 곂치는 곳 
# n2sum 은 (1, 1) 부터 (x,y) 까지의 합을 계산한 배열
# S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j]
"""

n2sum = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1): 
    for j in range(1, n+1): 
        n2sum[i][j] = n2list[i][j] + n2sum[i-1][j] + n2sum[i][j-1] - n2sum[i-1][j-1]

# from pprint import pprint
# pprint(n2list)
# pprint(n2sum)

def check_sum(x1, y1, x2, y2): 
    global n2sum
    result = n2sum[x2][y2] - n2sum[x1-1][y2] - n2sum[x2][y1-1] + n2sum[x1-1][y1-1]
    return result

for i in range(m):
    x1, y1, x2, y2 = map(int, input().strip().split())
    print(check_sum(x1, y1, x2, y2))
import sys
input = sys.stdin.readline 

n = int(input())
m = int(input())
xlst = list(map(int, input().strip().split())) # m개의 x

result = 0
for i in range(1, m): 
    x_diff = (xlst[i] - xlst[i-1] + 1)//2 # 반올림
    if x_diff > result: 
        result = x_diff

if xlst[0] > result: 
    result = xlst[0]
if n-xlst[-1] > result: 
    result = n-xlst[-1]

print(result)
import sys
input = sys.stdin.readline 

N = int(input())
size = [tuple(map(int, input().strip().split())) for _ in range(N)]
# N = 5
# size = [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]

# print(size)
result = [1]*N
for i in range(N):
    x, y = size[i][0], size[i][1] 
    for j in range(N): 
        if size[j][0] > x and size[j][1] > y: 
            result[i] += 1

print(*result)
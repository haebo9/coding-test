import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

# i부터 j까지의 합 = j까지의 합 - (i-1)까지의 합
range_sum = [0]

temp_sum = 0
for i in map(int, input().strip().split()):
    temp_sum += i
    range_sum.append(temp_sum)

for _ in range(m):
    i, j = map(int, input().strip().split())
    result = range_sum[j] - range_sum[i-1]
    print(result)
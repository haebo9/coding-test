import sys
input = sys.stdin.readline 

n = int(input())
array = list(map(int, input().strip().split()))

curr_max = array[0]
total_max = array[0]

for i in range(1,n):
    curr_max = max(curr_max + array[i], array[i])
    total_max = max(curr_max, total_max)

print(total_max)
import sys
input = sys.stdin.readline 

nums = [int(input()) for i in range(int(input()))]
sorted_nums = sorted(nums)
print(*sorted_nums, sep='\n')
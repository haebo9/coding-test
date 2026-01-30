import sys 
input = sys.stdin.readline 

nums = [int(input()) for i in range(int(input()))]
sorted_nums = sorted(nums)

# 산술 평균 
print(int(round(sum(nums)/len(nums),0)))

# 중앙값
print(sorted_nums[len(nums)//2])

# 최빈값 
from collections import Counter
counter = Counter(sorted_nums).most_common(2)
print(counter[-1][0] if counter[0][1] == counter[-1][1] else counter[0][0])

# 범위
print(sorted_nums[-1] - sorted_nums[0])
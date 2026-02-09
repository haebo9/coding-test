import sys
input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().strip().split()))

m = int(input())
target = list(map(int, input().strip().split()))

result = [1 if t in nums else 0 for t in target ]
print(*result)
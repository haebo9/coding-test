import sys
input = sys.stdin.readline 

a, b = map(int, input().strip().split())
aset = set(input().strip().split())
bset = set(input().strip().split())

result = (aset | bset) - (aset & bset)
print(len(result))
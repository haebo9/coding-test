import sys
input = sys.stdin.readline

strings = input().strip()
n = len(strings)

result = set()
for i in range(1, n+1):
    for j in range(0, n+1-i):
        result.add(strings[j:j+i])

print(len(result))
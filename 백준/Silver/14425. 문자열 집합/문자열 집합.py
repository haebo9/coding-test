import sys
input = sys.stdin.readline 

# 교집합
n, m = map(int, input().strip().split())

S = set([input().strip() for i in range(n)])
Target = list([input().strip() for i in range(m)])

# Target에 중복된 입력이 들어올 가능성이 있음 
result = 0
for i in Target: 
    if i in S: 
        result += 1
print(result)
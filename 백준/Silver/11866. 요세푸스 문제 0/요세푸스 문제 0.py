from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n+1))
result = []

while q: 
    for i in range(1, k+1):
        temp = q.popleft()
        if i != k: 
            q.append(temp)
        else: 
            result.append(temp)

result = f"<{', '.join(map(str, result))}>"
print(result)
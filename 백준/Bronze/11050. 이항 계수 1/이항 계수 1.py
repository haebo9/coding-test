import math
n, k = map(int, input().split())

result = math.factorial(n) // (math.factorial(n-k) * math.factorial(k))
print(result)
lst = [input().strip().split('-')[1] for _ in range(int(input()))]
result = sum(map(lambda x: int(x) <= 90, lst))
print(result)
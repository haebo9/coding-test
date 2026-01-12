a,b = map(lambda x: int(''.join(list(x)[::-1])), input().split())
print(max(a,b))

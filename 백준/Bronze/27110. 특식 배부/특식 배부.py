n = int(input())
lst = list(map(int, input().strip().split()))

result = [max(0,i-n) for i in lst]
print(sum(lst) - sum(result))
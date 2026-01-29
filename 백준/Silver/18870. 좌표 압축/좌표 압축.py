import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().strip().split()))
set_lst = sorted(set(lst))

dic = { x : i for i, x in enumerate(set_lst) }
# print(dic)

lst = [dic[i] for i in lst]
print(*lst)
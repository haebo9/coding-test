import sys

# 알파벳을 알려주면 그걸 찾아서 분리 => 배열
alp = {'c=':'A', 'c-':'B', 'dz=':'C', 'd-':'D', 'lj':'E', 'nj':'F', 's=':'G', 'z=':'H'}

# user = input()
user = sys.stdin.readline().strip()

for k, v in alp.items():
    # print(k, v)
    user = user.replace(k, v)

print(len(user))
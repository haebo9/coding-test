n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)
for _ in range(n):
    temp = list(map(int, input().split()))
    b.append(temp)

# print(a)
# print(b)

for i in range(n):
    temp = []
    for j in range(m):
        temp.append(a[i][j] + b[i][j])
    print(*temp)
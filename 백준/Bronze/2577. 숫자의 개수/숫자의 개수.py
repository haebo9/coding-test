a, b, c = [int(input()) for _ in range(3)]

cnt = {str(i) : 0 for i in range(10)}

for i in list(str(a*b*c)):
    cnt[i] += 1

print(*cnt.values(), sep= '\n') 
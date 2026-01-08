n = int(input())

for _ in range(n):
    r, s = input().split()
    r = int(r)

    print(''.join(list(map(lambda x: x*r,list(s)))))
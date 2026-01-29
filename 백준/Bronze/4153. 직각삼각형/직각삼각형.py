def tri_check(a,b,c) : 
    if c**2 == a**2 + b**2 : 
        return 'right'
    else: 
        return 'wrong'

while True: 
    tri = map(int, input().strip().split())
    a, b, c = sorted(tri)
    if a==0 and b == 0 and c == 0 : 
        break
    else:
        print(tri_check(a,b,c))

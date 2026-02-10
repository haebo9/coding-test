"""
ax + by = c
dx + ey = f

# 1
adx + bdy = cd
adx + aey = fa

y = (f*a - c*d) / (a*e - b*d)
x = (c - b*y)/a

# 2
eax + eby = ec
bdx + bey = bf

x = (e*c-b*f) // (e*a - b*d)
y = (c-a*x) // b

"""
import sys
input = sys.stdin.readline

a,b,c,d,e,f = list(map(int, input().strip().split()))

try: 
    y = (f*a - c*d) // (a*e - b*d)
    x = (c - b*y) // a
except : 
    x = (e*c-b*f) // (e*a - b*d)
    y = (c-a*x) // b

print(x, y)
import sys
input = sys.stdin.readline 

x, y, w, h = map(int, input().strip().split())

d_hori = min(x-0, w-x)
d_verti = min(y-0, h-y)

print(min(d_hori, d_verti))
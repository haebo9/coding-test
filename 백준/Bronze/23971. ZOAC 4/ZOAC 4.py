H, W, N, M = map(int,input().strip().split())

r = 0 
c = 0

for _ in range(0, H, N+1): 
    r += 1

for _ in range(0, W, M+1): 
    c +=1 

print(r*c)
import sys
input = sys.stdin.readline

s = input().strip()
q = int(input().strip())

n = len(s)

alpha_tf = {i: [0]*n for i in s}
for i,x in enumerate(s): 
    alpha_tf[x][i] = 1

# print(alpha_tf)

for _ in range(q):
    a, i, j = input().strip().split()
    if a in alpha_tf.keys(): 
        result = sum(alpha_tf[a][int(i):int(j)+1])
        print(result)
    else: 
        print(0)
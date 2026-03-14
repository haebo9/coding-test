import sys
input = sys.stdin.readline 

n = int(input())
pillar = [tuple(map(int, input().strip().split())) for _ in range(n)]

# n = 7
# pillar = [(2, 4), (11, 4), (15, 8), (4, 6), (5, 3), (8, 10), (13, 6)]

############
p = sorted(pillar)

left = p[0][1]
right = p[-1][1]
h_top = sorted(pillar, key=lambda x: x[1])[-1]

# 왼쪽 끝에서 최고점까지 상승하는 기둥만
curr_top = 0
up = []
for i in p:
    l, h = i
    if h > curr_top: 
        curr_top = h
    if curr_top == h: 
        up.append(i)  
    if l == h_top[0]: 
        break 

# 오른쪽 끝에서 최고점까지 상승하는 기둥반 (반대로 하락)
curr_top = 0
dn = []
for i in reversed(p): 
    l, h = i
    if h > curr_top: 
        curr_top = h
    if curr_top == h: 
        dn.append(i)
    if l == h_top[0]: 
        break 
dn.reverse()

############# 
# 최고점 값으로 시작
result = h_top[1]

# 기둥 높이 계산
if len(up) >= 2: 
    for i in range(len(up)-1): # 상승 높이 
        result += (up[i+1][0] - up[i][0])*(up[i][1])

if len(dn) >= 2: 
    for i in range(len(dn)-1): # 하락 높이 
        result += (dn[i+1][0] - dn[i][0])*(dn[i+1][1])

print(result)
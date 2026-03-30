import sys
input = sys.stdin.readline 

n = int(input())

result_h = [0,0]
result = [0] * 5

step = 1
for i in range(n): 
    row = list(input().strip())

    # 머리 위치, 심장 위치 찾기  
    if step == 1: 
        if '*' in row: 
            heart = (i+1, row.index('*'))
            result_h = [heart[0]+1, heart[1]+1]
            step += 1
            continue

    # 팔 길이 찾기 
    elif step == 2: 
        result[0] = heart[1] - row.index('*')
        result[1] = (n-1 - row[::-1].index('*')) - heart[1]
        step += 1
        continue
    
    # 허리 찾기
    elif step == 3 and row[heart[1]]=='*': 
        result[2] += 1

    # 왼쪽 다리 
    else: 
        if row[heart[1]-1]=='*': 
            result[3] += 1
        if row[heart[1]+1]=='*': 
            result[4] += 1

print(*result_h)
print(*result) 
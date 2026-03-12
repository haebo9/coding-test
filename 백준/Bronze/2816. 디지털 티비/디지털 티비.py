# import sys
# input = sys.stdin.readline 

N = int(input())
arr = [input().strip() for _ in range(N)]
# N = 4
# arr = ['ABC1', 'ABC02', 'KBS2', 'KBS1']

idx = 0
k1,k2 = -1, -1
# print(arr, idx)
result = []

# 명령 수행 함수 
def order(o): 
    global idx, arr
    if o == 1: 
        idx += 1
    elif o == 2: 
        idx -= 1
    elif o == 3:
        arr[idx], arr[idx+1] = arr[idx+1], arr[idx] 
        idx += 1
    elif o ==4: 
        arr[idx], arr[idx-1] = arr[idx-1], arr[idx] 
        idx -= 1
    # print('order: ', o)
    result.append(o)

# KBS1, KBS2의 위치 찾기 
for i, a in enumerate(arr): 
    if a == 'KBS1': 
        k1 = i
    elif a == 'KBS2': 
        k2 = i
    if k1 != -1 and k2 != -1: 
        break 

# print('k1,k2 = ', k1, k2)

# 어떻게든 두 값을 옮기기 
cnt = 0
while arr[idx] !=  'KBS1': 
    
    if arr[idx+1] == 'KBS1': 
        order(1)
        while k1 != 0: 
            order(4)
            k1 -=1 
    else: 
        order(3)

# print(arr, idx)
order(1)
while arr[idx] !=  'KBS2': 
    
    if arr[idx+1] == 'KBS2': 
        order(1)
        while k2 != 1: 
            order(4)
            k2 -=1
    else: 
        order(3)

print(*result, sep='')
# print(arr)
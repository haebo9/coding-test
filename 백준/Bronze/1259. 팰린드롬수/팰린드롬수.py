def pell(num:str): 
    lst = list(num)
    mid = len(lst)//2

    if len(lst) % 2 == 0:         
        left = lst[:mid]
        right = lst[mid:][::-1]
    else: 
        left = lst[:mid]
        right = lst[mid+1:][::-1]

    return ('yes' if left==right else 'no')

import sys
input = sys.stdin.readline 

while True: 
    num = input().strip() # 출력초과 방지 
    if num == '0': 
        break 
    else: 
        print(pell(num))
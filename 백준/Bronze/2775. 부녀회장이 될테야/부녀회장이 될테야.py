def all_num(): 
    "아파트 층수별 사람 수 계산"
    # 0층의 i호에는 i명이 산다. 
    apt = [list(range(1, 14+1))]
    # print(apt)

    for i in range(1, 14+1): # 층수 
        apt_i = []
        temp = 0 
        for j in range(14): # 호수 
            temp += apt[i-1][j]
            apt_i.append(temp)
        apt.append(apt_i)

    return apt

import sys
input = sys.stdin.readline 

apt = all_num()

t = int(input())
for _ in range(t):
    k =int(input())
    n =int(input())
    print(apt[k][n-1])
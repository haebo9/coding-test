def spiral(n): 
    """
    숫자는 변의 길이가 아니라 P(N)의 번호
    1 = 1
    2 = 1
    3 = 2
    4 = 1+3
    5 = 4
    6 = 3+5
    7 = 2+6
    8 = 1+7
    9 = 4+8 
    10 = 5+9
    11 = 6+10
    12 = 7+11
    """
    pn = [0,1,1,1,2,2,3,4,5,7,9]
    if n <= 10: 
        return pn[n]
    else: 
        for i in range(11, n+1): 
            pn.append(pn[i-1] + pn[i-5])
        return pn[n]

import sys
input = sys.stdin.readline 

for _ in range(int(input())):
    n = int(input())
    print(spiral(n))
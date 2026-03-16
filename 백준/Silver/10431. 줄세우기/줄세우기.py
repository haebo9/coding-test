def solution(arr): 
    result = []
    cnt = 0
    for i, a in enumerate(arr): 
        result.append(a)
        chk = i
        while chk > 0: 
            if result[chk-1] > result[chk]: 
                result[chk-1], result[chk] = result[chk],result[chk-1]
                chk -= 1
                cnt +=1 
            else: 
                break 
    # print(result)
    return cnt

import sys
input = sys.stdin.readline 

for _ in range(int(input())): 
    t, *arr = list(map(int, input().strip().split()))

    print(t, solution(arr))
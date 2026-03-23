import sys
input = sys.stdin.readline 

k, n = map(int, input().split())
klist = [int(input()) for _ in range(k)]

def cnt_len(klist, mid): 
    cnt = 0
    for x in klist: 
        cnt += x//mid
    return cnt

def dev_conq(k, n, klist): 
    s = 1
    e = max(klist)
    result = 0

    while s <= e: 
        mid = (s + e)//2
        cnt = cnt_len(klist, mid)
        # 너무 많이 만들어짐 = 나눈 길이가 너무 짧다 or 딱 맞게 
        if cnt >= n: 
            s = mid+1
            result = max(result, mid)
        # 너무 적게 만들어짐 = 나눈 길이가 너무 길다
        else: 
            e = mid-1
    
    return result 

print(dev_conq(k, n, klist))
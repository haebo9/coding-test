def room_ck(h,w,n):
    
    floor = (h if n % h == 0 else n % h)
    num = (n // h if n % h == 0 else n // h + 1)

    floor = str(floor)
    num = str(num) if num >= 10 else f'0{num}' 
    return floor+num

import sys 
input = sys.stdin.readline

T = int(input()) # 테스트 횟수 

for _ in range(T):
    H,W,N = map(int, input().strip().split()) # 층수, 방수, 몇번째 
    print(room_ck(H,W,N))
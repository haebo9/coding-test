import sys
input = sys.stdin.readline

import heapq 

def middle(c, up_mid, dn_mid):
    # 최소힙이 개수가 적으면 up에 기본으로 들어감
    if len(up_mid) <= len(dn_mid):
        heapq.heappush(up_mid, c)
    
    # 최대힙이 개수가 적으면 dn에 기본으로 들어감
    elif len(up_mid) > len(dn_mid):
        heapq.heappush(dn_mid, -c)
        
    # 최대힙의 루트 값이 최소힙의 루트보다 커지면 교체 
    while up_mid and dn_mid and up_mid[0] < -dn_mid[0]: 
        top = heapq.heappop(up_mid)
        down = -heapq.heappop(dn_mid)
        heapq.heappush(dn_mid, -top)
        heapq.heappush(up_mid, down)

    return up_mid[0]


def check(m, nums): 
    up_mid = [] # 중앙값 보다 큰 수들 : 최소힙
    dn_mid = [] # 중앙값 보다 작은 수들 : 최대힙

    # 값을 하나씩 넣어주다가 홀수 번호에서 중앙값 저장
    mid = []
    for i, c in enumerate(nums):
        if i % 2 ==0: 
            mid.append(middle(c, up_mid, dn_mid))  
        else: 
            middle(c, up_mid, dn_mid)

    # 10개씩 끊어서 출력
    l = len(mid) ; print(l)
    start, end = 0, 10
    for _ in range(l//10 + 1):
        print(*mid[start:min(end, l)]) 
        start, end = start + 10, end + 10

# 10개씩 끊어서 입력 / 결과 반환
for _ in range(int(input())):
    m = int(input())
    nums = []
    for _ in range(m//10 +1):
        nums.extend(map(int, input().strip().split()))
    check(m, nums)
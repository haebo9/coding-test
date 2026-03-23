import sys
input = sys.stdin.readline 

# 칭호 맵핑 
n, m = map(int, input().split())

narr = []
for i in range(n):
    t, p = input().split()
    narr.append((t,int(p)))

# 이진검색으로 경계값 찾기
def mapping(p):
    low = 0
    high = n-1
    res = 0
    
    while low <= high: 
        mid = (low + high ) //2
        # 만약에 중간값이 목표값보다 크다면 한칸 내린곳 까지 재확인
        if p <= narr[mid][1]: 
            res = mid 
            high = mid - 1
        # 만약에 중간값이 목표값보다 작다면 큰 값만 확인
        else: 
            low = mid + 1
    
    return narr[res][0]

# power 매핑 
for _ in range(m): 
    p = int(input())
    print(mapping(p))
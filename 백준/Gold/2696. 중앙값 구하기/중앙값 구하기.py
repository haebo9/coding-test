import sys
input = sys.stdin.readline
# t = int(input())

# 홀수 번째 읽었을 때 중앙값 출력 
    # 수열의 크가 9 
    # 출력 번호 : 1 3 5 7 9 
    # 인덱스 값 : 0 2 4 6 8
    # 중앙 번호 : 1 2 3 4 5
    # 중앙인덱스 : 0 1 2 3 4

def middle(m:int, nums:list): 
    check = list(map(lambda x: x, range(0, m+1, 2)))
    mid = [sorted(nums[:i+1])[i//2] for i in check]
    
    l = len(mid) ; print(l)
    start, end = 0, 10
    for _ in range(l//10 + 1):
        print(*mid[start:min(end, l)]) 
        start, end = start + 10, end + 10
        


for _ in range(int(input())):
    m = int(input())
    nums = []
    for _ in range(m//10 +1):
        nums.extend(map(int, input().strip().split()))
    middle(m, nums)
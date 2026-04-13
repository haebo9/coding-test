import sys
input = sys.stdin.readline 

def solution(n, arr): 
    "전략 : 2차원 dp를 사용해서 현재 위치 기준 커지는 값 중 최대를 0번에 작아지는 값중 최대를 1번에 저장"

    dp = [[0]*2 for _ in range(n)]

    for i in range(0, n): # 0~n-1
        for j in range(0, i): # 0~i-1
            # j < i / i 이전까지의 j는 증가하는 방향의 최대 
            if arr[j] < arr[i]: 
                dp[i][0] = max(dp[i][0], dp[j][0]+1)

    for i in range(n, -1, -1): # 0~n-1
        for j in range(n-1, i, -1): # n-1 ~ i+1 
            # print(i, j)
            # i < j / i 이후 j는 감소하는 방향의 최대 
            if arr[j] < arr[i]: 
                dp[i][1] = max(dp[i][1], dp[j][1]+1)

    result = max([x+y+1 for x,y in dp])
    return result

n = int(input())
arr = list(map(int, input().strip().split()))

# n = 11
# arr = [1,2,3,4,5,6,7,6,5,4,8] # 10이 정답 
print(solution(n, arr))
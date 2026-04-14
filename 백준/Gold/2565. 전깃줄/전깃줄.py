import sys
input = sys.stdin.readline 

def solution(k, arr): 
    "1번부터 끝번호 까지 교차하지 않고 연결할 수 있는 전기줄의 개수를 저장한다.(dp)"
    # 연결 선 시작점 기준 정렬 
    arr.sort()

    n = 500 # 번호 최댓값
    dp = [0]*(n+1)
    lines = [0]*(n+1)

    # lines에 전깃줄 연결 상태 저장 
    for i, c in arr: # i -> c로의 전깃줄 연결 
        # 인덱스는 출발 위치의 번호, 인덱스에서의 값은 연결된 전깃줄의 번호 
        lines[i] = c
        dp[i] = 1 # 전깃줄 연결된 곳은 이미 1개 연결 

    # 각 위치에서의 연결 가능한 전봇대 줄 수 저장 
    for i, c in arr: 
        for j, _ in arr: # 1~i-1
            # 비교 범위 지정 
            if j > i: 
                break
            # 현재 값보다 작은 값 중에서 최대 + 1
            if c > lines[j] and lines[j]: 
                dp[i] = max(dp[j]+1, dp[i])

    return k - max(dp) # 제거해야 하는 전기줄 수 계산 

k = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(k)]
print(solution(k, arr))
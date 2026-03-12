#### Greedy ####

import sys
input = sys.stdin.readline 

N = int(input())
butget = list(map(int, input().strip().split()))
M = int(input())

def solution(N, butget, M):
    # 오름차순 정렬 
    butget = sorted(butget)

    # 예산이 부족하지 않음 
    if M >= sum(butget): 
        # 예산 요구액 중 최댓값을 반환
        return max(butget)

    # 최소 1개가 예산이 부족함
    else: 
        # 필요 예산이 최소 기준값을 초과하는 경우
        avg = M // N 

        # 전체 예산에서 예산이 충분한 지방을 배분
        # (주의! 중복된 예산값이 들어올 수 있음) 80 80 101 101 / M = 360  
        for i in range(N): 
            avg = M // N

            if butget[i] <= avg: 
                M -= butget[i]
                N -= 1
            else: 
                # 남은 금액을 초과된 지방에 배분
                # 남은 예산 중에서 초과되는 지방의 수만큼 배분 (상한액)
                return avg

print(solution(N, butget, M))
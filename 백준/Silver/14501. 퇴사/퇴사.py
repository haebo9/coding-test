# 백트래킹 : 앞에서 부터 쭉 진행을 하여 값을 갱신한다. 선택지 : 한다 안한다 / 끝에 도달하면 뒤로 돌아옴
import sys
input = sys.stdin.readline 

n = int(input().strip())
lst = [tuple(map(int, input().strip().split())) for _ in range(n)]

result = 0

def backtrack(idx, get): 
    global result

    # 종료 조건 : 범위가 끝에 도달
    if idx == n: 
        result = max(result, get)
        return 
    
    # 종료 조건 : 범위가 끝을 넘음
    if idx > n: 
        return 
    
    # 다음 날짜로 이동 조건 (이동 가능한 경우) 
    time, pay = lst[idx]
    if idx + time <= n: 
        backtrack(idx + time, get + pay) 

    # 다음 위치로 이동시 범위를 넘어가는 경우 (현재 날짜에서 종료)
    else: 
        result = max(result, get)

    # 현재 날짜를 건너띄는 경우 (중요)
    backtrack(idx+1, get)

backtrack(idx=0, get=0)
print(result)
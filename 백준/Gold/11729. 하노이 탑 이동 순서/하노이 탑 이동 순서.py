"""
하노이의 탑 : 1번 장대에서 3번 장대로 원판을 옮기기 

3번으로 1번 원판 옮기고 
2번으로 2번 원판 옮기고 
3번에 있는 1번 원판을 2번으로 옮기고
"""

def hanoi(n, stt, mid, end):
    global cnt, result
    """hanoi() 함수는 n개의 원판을 종점으로 옮긴다."""
    if n == 1: 
        cnt += 1
        result.append((stt, end))
        return

    # stt의 가장 큰 원판을 제외하고 나머지를 중간 지점으로 옮긴다. (종점 경유) 
    hanoi(n-1, stt, end, mid)

    # 가장 큰 원판을 종점으로 옮긴다. 
    cnt += 1
    result.append((stt, end))

    # 중간 지점에 있던 나머지 원판을 종점으로 옮긴다. (시작점 경유) 
    hanoi(n-1, mid, stt, end)

import sys
input = sys.stdin.readline 

n = int(input())
cnt = 0
result = []
stt, mid, end = 1, 2, 3
hanoi(n, stt, mid, end)

print(cnt)
for i in result: 
    a, b = i
    print(a, b)
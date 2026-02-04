import sys
input = sys.stdin.readline 

# 현재 시점에서 가장 빨리 끝나는 회의부터 진행하는 것
n = int(input())
scrum = []

for _ in range(n):
    s, e = map(int, input().strip().split())
    scrum.append((s,e))

def check_scrum(scrum): 
    scrum = sorted(scrum, key = lambda x: (x[1], x[0]))

    curr_time = 0 # 현재 시간(마지막 종료 시작) 
    cnt = 0 # 회의 갯수

    for i in scrum: 
        s, e = i[0], i[1]
        if s >= curr_time: 
            curr_time = e
            cnt += 1

    return cnt

print(check_scrum(scrum))
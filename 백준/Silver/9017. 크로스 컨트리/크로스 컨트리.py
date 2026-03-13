from collections import Counter
def winner(n, arr): 
    "순위별 팀번호 배열이 입력되었을 때 우승팀을 찾는 함수" 
    total_cnt = Counter(arr)
    team_cnt = len(total_cnt)

    cnt = [0]*(team_cnt+1)
    scores = [0]*(team_cnt+1)
    fivth = [1000]*(team_cnt+1)

    # i+1는 순위(점수), a는 팀 번호
    rank = 1
    for i, a in enumerate(arr): 
        cnt[a] += 1
        # 팀별 네 번째 선수까지만 점수 저장 
        # 6명 기준에 부합할 때만 점수 부여 및 갱신
        if total_cnt[a] == 6: 
            if cnt[a] <= 4:
                scores[a] += rank
            rank += 1
                
        # 팀별 다섯 번째 선수의 순위 저장
        if cnt[a] == 5: 
            fivth[a] = (i+1) 

    min_s = float('inf')
    winner = int
    # a은 팀번호, s는 팀별 점수
    for a, s in enumerate(scores): 
        # index=0 이거나 팀 인원이 6명이 안되면 예외처리
        if a == 0 or total_cnt[a] < 6: 
            continue
        # 점수가 작은 것이 이기는 것
        if s < min_s:
            min_s = s
            winner = a
        # 동점 처리 
        elif s == min_s: 
            if fivth[a] < fivth[winner]: 
                winner = a

    return winner

import sys
input = sys.stdin.readline 

t = int(input())
for _ in range(t): 
    n = int(input())
    arr = list(map(int, input().strip().split()))

    print(winner(n, arr))
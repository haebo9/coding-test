# 전략 : 생성된 방의 정보를 담은 stack을 만들고 앞에서 부터 상태 확인하며 방을 채운다. 
import sys
input = sys.stdin.readline 

p, m = map(int, input().split())

stack = []

for _ in range(p): # 플레이어 수 만큼 확인 
    l, n = input().split()
    l = int(l)
    # 방이 하나도 없으면 새로 방 만들어 넣음
    if not stack: 
        stack.append([(l, n)])
    else: 
        # 기존의 방을 앞에 부터 순회하며 조건 맞으면 입장
        for i, s in enumerate(stack): 
            # 방의 길이조건 및 레벨 범위 조건 
            if (len(s) < m) and (s[0][0] - 10 <= l and l <= s[0][0] + 10): 
                s.append((l, n))
                break 
        # 모든 방을 확인했음에도 조건에 맞는 것이 없으면 새로 방 생성
        else: 
            stack.append([(l, n)])

# 방이 생성된 순서대로 출력 
for i, s in enumerate(stack): 
    s = sorted(s, key = lambda x: x[1]) # 닉네임 사전순 정렬 
    print('Started!' if len(s) == m else 'Waiting!')
    for ss in s: 
        print(*ss)
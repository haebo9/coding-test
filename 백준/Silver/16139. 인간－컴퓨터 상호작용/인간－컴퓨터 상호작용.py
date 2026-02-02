import sys
input = sys.stdin.readline

s = input().strip()
q = int(input().strip())
set_s = set(s) 
n = len(s)

# 1. 모든 알파벳에 대해 미리 누적 합 리스트를 생성 (n+1 크기 권장)
alpha_tf = {chr(c): [0] * (n + 1) for c in range(ord('a'), ord('z') + 1)}

# 2. 문자열을 딱 한 번만 순회 (O(N))
for i, char in enumerate(s):
    # 우선 모든 알파벳의 이전 값을 현재 칸으로 복사
    for char_key in set_s:
        alpha_tf[char_key][i + 1] = alpha_tf[char_key][i]
    
    # 현재 위치의 문자에 대해서만 1을 더함
    alpha_tf[char][i + 1] += 1

# print(alpha_tf)

start = 'a'
target = alpha_tf[start]
for _ in range(q):
    a, i, j = input().strip().split()
    if a in set_s: 
        if  a != start: 
            start = f'{a}'
            target = alpha_tf[start]
        target = alpha_tf[a]
        i, j = int(i)+1, int(j)+1
        print(target[j] - target[i-1])

    else: 
        print(0)
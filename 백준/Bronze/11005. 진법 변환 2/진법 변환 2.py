def to_B(N, B):
    if N == 0: return [0] # N이 0인 경우 예외 처리
    
    # 1. N보다 작거나 같은 B의 가장 큰 거듭제곱(i) 찾기
    i = 0
    while B**(i + 1) <= N:
        i += 1
    
    answer = []
    # 2. 찾은 최대 자릿수(i)부터 0까지 내려가며 계산
    for j in range(i, -1, -1):
        answer.append(N // (B**j))
        N %= (B**j)
    return answer

def to_alp(answer):
    # 리스트 컴프리헨션으로 숫자는 str, 10 이상은 알파벳 변환
    return [chr(i + 55) if i >= 10 else str(i) for i in answer]

# 입력 및 실행
import sys
input = sys.stdin.readline

line = input().split()
if line:
    N, B = map(int, line)
    result_list = to_B(N, B)
    result_str = to_alp(result_list)
    print(''.join(result_str))
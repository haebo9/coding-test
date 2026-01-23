# 알파벳 대문자-> 숫자 리스트
def alp_to_numlist(alp):
    # A가 10, Z가 35
    return list(map(lambda x: int(x) if x.isdigit() else ord(x)-55, list(alp)))

# 진법 변환 B -> 10 진법
def B_to_10(alp:list, B:int) -> int: 
    result = 0
    for i, a in enumerate(alp[::-1]):
        result += a*(B**i)
    return result

import sys
input = sys.stdin.readline
N, B = input().split()

B = int(B)
alp = alp_to_numlist(N)
result = B_to_10(alp, B)

print(result)
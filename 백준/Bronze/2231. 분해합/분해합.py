"""
245(M)의 분해합이 256(N)일 때, M은 N의 생성자 
= 분해합이 N이 되는 생성자(M)의 최솟값을 구하라. 

생성자가 없는 경우? 어떻게 합쳐도 그 값이 안나옴
"""
import sys
input = sys.stdin.readline

N = int(input())
min_n = max(0, N - len(str(N))*9 - 1)

result = None
for i in range(min_n, N):
    temp = i + sum(map(int, list(str(i))))

    if temp == N: 
        result = i
        break

print(result if result else 0)
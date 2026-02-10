"""
245(M)의 분해합이 256(N)일 때, M은 N의 생성자 
= 분해합이 N이 되는 생성자(M)의 최솟값을 구하라. 

생성자가 없는 경우? 어떻게 합쳐도 그 값이 안나옴
"""
N = int(input().strip())

result = None
for i in range(N, 0, -1):
    temp = i + sum(map(int, list(str(i))))

    if temp == N: 
        result = i

print(result if result else 0)
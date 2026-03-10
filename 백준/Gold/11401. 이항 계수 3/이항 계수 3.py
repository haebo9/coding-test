# nCr = n! / (n-k)!*k! = n! * ((n-k)!*k!)**(P-2) 
def power(a, b): 
    " a의 b제곱승의 값을 분할 정복 방법으로 구하기 "
    if b == 0: 
        return 1

    half = power(a, b // 2)

    result = (half * half) % MOD

    if b % 2 != 0: # 홀수
        return ( result * a ) % MOD
    else: # 짝수 
        return result

import sys
input = sys.stdin.readline 

N, K = map(int, input().strip().split())
MOD = 1000000007

# N까지의 팩토리얼 값을 구함 
fact = [1] * (N+1)
for i in range(1, N+1):
    fact[i] = fact[i-1]*i % MOD

# nCr 값을 구함
# n! * ((n-k)!*k!)**(P-2) 
answer = fact[N] * power((fact[N-K]*fact[K]),MOD-2) % MOD
print(answer)
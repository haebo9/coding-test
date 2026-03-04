def b_squared(a,b,c):
    """
    A를 B번 곱한 수를 C로 나눈 나머지를 구하는 함수
    단, A, B, C는 모두 2,147,483,647 이하의 자연수이다. 

    전략 : A를 가능한 작은 인자들로 나눠서 하나씩 곱해가며 나머지 값을 구한다. 
    a % c = ( a//k * k ) % c = ( (a//k % c) * (k % c) ) % c => 모듈러 연산 
    """
    if b == 1: 
        return a % c
    
    if b == 0: 
        return 1

    
    # A^B 을 A^(B/2) * A^(B/2) 로 일단 나눈 뒤 연산
    temp = b_squared(a, b//2, c)

    if b % 2 == 0: 
        return ( (temp % c) * (temp % c) ) % c
    
    else: 
        return ( (temp % c) * (temp % c) * b_squared(a, 1, c)) % c

import sys
input = sys.stdin.readline 

a,b,c = map(int, input().strip().split())
print(b_squared(a, b, c))
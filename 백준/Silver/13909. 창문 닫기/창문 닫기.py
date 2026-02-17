def window(n):
    """
    # 1~N번 까지 자신의 배수 번째 창문을 열려있으면 닫고, 닫혀있으면 여는 로직을 반복 

    사실상 n번째 창문의 열림 여부는 약수의 개수를 구하는 것과 같다. 
        약수가 홀수 : 열림(True)
        약수가 짝수 : 닫힘(False)

    약수의 개수가 홀수가 되기 위한 조건 : 완전 제곱수 only (k * k)
    다른 약수는 (3 x 4) (4 x 3) 처럼 쌍을 이루게 됨 = 짝수 개수 
    """
    # 제곱수 square(n)의 정수 값의 최댓값 square(n)**2 = n 
    # square(n)의 정수값 보다 작은 정수의 개수만큼 완전 제곱수 존재 
    result = int(n**0.5)
    return result 

import sys
input = sys.stdin.readline 
n = int(input())
print(window(n))
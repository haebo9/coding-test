def fraction_sum(a1, b1, a2, b2):
    """ 
    두 분수의 합을 구하는 함수. 최대공약수를 구해서 최대공배수를 구한다. 

    분모 : 최대 공배수
    분자 : 각 분수의 분모에 곱해서 최대 공배수가 되는 값

    출력된 두 분수의 합이 기약분수 라는 것을 보장해야 한다. 
    """
    def get_gcd(b1, b2):
        """최대공약수 : 유클리드 호제법""" 
        while b2:
            b1, b2 = b2, b1%b2
        return b1
    
    def get_lcm(b1, b2):
        """최소공배수 : 중복 없는 소인수 곱""" 
        return b1*b2 // get_gcd(b1,b2)

    def result(numerator, denominator): # 분자, 분모 순으로 입력
        """ 분수가 기약분수가 되도록 처리 """
        gcd = get_gcd(denominator, numerator)
        if gcd == 1: 
            return numerator, denominator
        else: 
            return numerator//gcd, denominator//gcd

    
    denominator = get_lcm(b1, b2) # 동일한 분모
    numerator = a1*denominator//b1 + a2*denominator//b2 # 분자합
    
    numerator, denominator = result(numerator, denominator)
    return numerator, denominator

import sys
input = sys.stdin.readline 

a1, b1 = map(int, input().strip().split())
a2, b2 = map(int, input().strip().split())

print(*fraction_sum(a1, b1, a2, b2))
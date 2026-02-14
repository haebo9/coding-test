# 최대 공약수
def get_gcd(a, b): 
    """
    유클리드 호제법 : a와 b의 공약수는, b와 (a를 b로 나눈 나머지)의 공약수와 같다. 
    
    나머지를 구해 숫자의 덩치를 줄여나가도 공약수 성질은 변하지 않음. 
    GCD(12, 8) = GCD(8, 4) = GCD(4, 0)
    """
    while b: 
        a, b = b, a%b
    return a

# 최대 공배수
def get_lcm(a, b): 
    """ 최대공약수로 a와 b중 하나만 나눠준 뒤 곱한 수 """
    return a*b // get_gcd(a, b)

# 케이스 입력
import sys
input = sys.stdin.readline 

for _ in range(int(input())): 
    a,b = map(int, input().strip().split())
    print(get_lcm(a,b))
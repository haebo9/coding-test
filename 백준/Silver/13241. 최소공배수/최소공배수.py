# 최대공약수
def get_gcd(a,b): 
    while b: 
        a, b = b, a%b
    return a

# 최대 공배수
def get_lcm(a, b): 
    return (a*b) // get_gcd(a, b)

import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split())
print(get_lcm(a,b))
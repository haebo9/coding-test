import sys
input = sys.stdin.readline 

def greatest_common_divisor(a, b): 
    "최대 공약수"

    while b: 
        a, b = b, a%b
    
    return a

def least_common_muliple(a,b): 
    "최소 공배수"

    return a*b // greatest_common_divisor(a, b)

t = int(input())
for _ in range(t): 
    a, b= map(int, input().split())
    print(least_common_muliple(a, b))
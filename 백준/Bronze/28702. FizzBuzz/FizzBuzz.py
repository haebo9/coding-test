# 연속된 3개의 수 

# 첫번쨰가 Fizz면 결과도 Fizz
# 첫번째가 숫자면 결과는 첫번쨰 +3
# 두번쨰가 숫자면 결과는 두번쨰 +2
# 세번쨰가 숫자면 결과는 세번쨰 +1

# import sys
# input = sys.stdin.readline 

def solution(a,b,c):
    if a == 'FizzBuzz': 
        result = 'Fizz'
        return result 

    if a.isdigit(): 
        result = int(a)+3
    elif b.isdigit(): 
        result = int(b)+2
    elif c.isdigit(): 
        result = int(c)+1
        
    if result % 5 == 0: 
        if a == 'Fizz': 
            result = 'FizzBuzz'
        else: 
            result = 'Buzz'
    else: 
        if a == 'Fizz': 
            result = 'Fizz'
            
    return result

a,b,c = [input().strip() for _ in range(3)]
print(solution(a,b,c))
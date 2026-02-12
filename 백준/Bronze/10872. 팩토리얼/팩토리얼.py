n = int(input())

def factor(n): 
    if n == 1 or n == 0: 
        return 1
        
    return n*factor(n-1)

# n을 넣으면 n! 이 출력되는 함수
print(factor(n))
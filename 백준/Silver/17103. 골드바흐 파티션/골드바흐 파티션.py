# 전략 : N의 최대값(10^6) 까지의 소수 여부를 담은 리스트를 정의한 뒤 조회 
# decimal a, b: a + b = N <=> b = N - a, b가 소수인지 조회 

# 10^6 이하의 소수의 판별 여부(True,False)을 담은 배열을 반환
def decimal_array(): 
    max_n = 1000000
    array = [True]*(max_n+1)
    array[0] = array[1] = False
    for i in range(2, int(max_n**0.5)+1):
        if array[i]: 
            for j in range(i*i, max_n+1, i):
                array[j] = False

    primes = [i for i,x in enumerate(array) if x] # 소수인 값의 인덱스 저장
    return array, primes

# 배열의 합이 n이 되는 소수 합 조합 개수 반환 
def check_decimal_sum(n): 
    global array, primes
    result = 0

    for p in primes:
        if p > n//2: # 중복 방지 
            break 

        if array[n-p] : # a + b = n : 합이 n이 되는 b가 소수
            result += 1

    return result 

# 결과 반환 
import sys
input = sys.stdin.readline 

array, primes = decimal_array()

for _ in range(int(input().strip())):
    n = int(input().strip())
    print(check_decimal_sum(n))
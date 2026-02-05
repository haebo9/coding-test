import sys
input = sys.stdin.readline 

n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

# 연속된 숫자의 합이 m으로 나누어 떨어지는 경우의 수 
def sum_div():
    global n, m, nums
    """
    (S(i) - S(i+1)) % m = 0 <=>  S(i) % m = S(i+1) % m 
    일부 구간의 합이 m으로 나누어 떨어진다는 말은 일부 구간의 시작까지와 끝 까지의 합의 나머지가 서로 같다는 말

    나머지가 같은 수들의 조합 (각각의 경우에 2 수를 뽑는 경우) ; 순서 중복 주의 
    """

    # 나머지의 종류별 개수 
    rest = [0]*m 
    sum_i = 0
    for i in nums: 
        sum_i += i
        rest[sum_i % m] += 1

    # 1개 만으로도 조건 만족(나머지 0) 
    cnt = rest[0] 

    # 2개를 뽑아 조건 만족(구간)    
    for i in range(m): 
        cnt += ( rest[i] * (rest[i] -1) ) // 2
    
    return cnt

print(sum_div())
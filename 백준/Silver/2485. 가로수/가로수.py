def add_tree(curr):
    """
    기존의 나무들간의 간격을 찾음. 모든 나무 간격이 최소 간격이 되도록 나무를 추가해야함.

    1. 모든 나무 사이의 간격을 리스트로 담음
    2. 그리고 간격들의 최대공약수(gcd)를 구함. 
    3. 최대공약수로 모든 간격들을 나누고 그 합을 출력함
    """
    def get_multi_gcd(lst): 
        """ 최대 공약수를 갱신하며 최종값을 구함 """
        a = lst[0]
        for b in lst: 
            while b:
                a, b = b, a%b
        return a 
    
    dist = []
    for i in range(1, len(curr)): 
        dist.append(curr[i]-curr[i-1])
    
    gcd = get_multi_gcd(dist)
    result = list(map(lambda x: (x//gcd-1), dist))
    return sum(result)

import sys
input = sys.stdin.readline 

curr = [int(input()) for _ in range(int(input()))]
print(add_tree(curr))
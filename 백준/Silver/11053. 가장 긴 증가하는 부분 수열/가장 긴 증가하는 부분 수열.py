def dp():
    # i번째 까지의 부분수열의 최댓값 = i번으로 올 수 있는 값의 최댓값 + 1(자기 자신) 
    # i번으로 갈수 있는 i-k 번쨰의 값의 후보는 커질수만 있다. (작아지면 이미 포함됨)
    memo = [1]*(N)

    for i in range(1, N): 
        for j in range(i): 
            if array[j] < array[i]: 
                memo[i] = max(memo[i], memo[j] +1)

    return max(memo)

import sys
input = sys.stdin.readline 

N = int(input())
array = list(map(int, input().strip().split()))

print(dp())
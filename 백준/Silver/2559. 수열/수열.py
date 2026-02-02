# 온도 k개의 합이 모이면 현재까지 최대값과 비교 갱신 
def make_k_sum(temp, k): 
    from collections import deque

    cnt = 0
    sum_k = 0
    q = deque([])
    curr_max = -1000000

    for t in temp:
        cnt += 1 
        sum_k += t
        q.append(sum_k)
        if cnt == k+1:
            q_pop = q.popleft()
            cnt -= 1
            if curr_max < (q[-1] - q_pop): 
                curr_max = q[-1] - q_pop
        elif cnt == k: 
            if curr_max < (q[-1]): 
                curr_max = q[-1]
        # print(t, q, curr_max)
    return curr_max

# import sys
# input = sys.stdin.readline

n, k = map(int, input().strip().split())
temp = map(int, input().strip().split())
print(make_k_sum(temp, k))
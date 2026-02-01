# 두 큐를 정의하고 sum(O(N))의 결과가 더 큰 곳의 값을 빼서 작은 곳으로 옮는 과정 반복
from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    q1_total = sum(q1)
    q2_total = sum(q2)
    target = ( q1_total + q2_total ) // 2
    cnt = 0
    
    while q1 and q2: 
        if q1_total > q2_total: # q1 > q2
            temp = q1.popleft()
            q1_total -= temp
            q2_total += temp
            q2.append(temp)
            
        elif q1_total < q2_total: # q1 < q2
            temp = q2.popleft()
            q2_total -= temp
            q1_total += temp
            q1.append(temp)
        
        elif q1 == list(queue1) and q2 == list(queue2): # 순환 발생 시 조기 종료
            return -1 
            
        elif q1_total == q2_total: # q1 == q2
            return cnt
        
        cnt += 1
        if cnt >= 1000000: 
            return -1 
    else: 
        return -1
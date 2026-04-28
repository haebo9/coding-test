from collections import deque 

def solution(numbers, target):
    n = len(numbers)
    
    def num_bfs(numbers): 
        # 누적합에 사용될 배열
        num = deque(numbers)
        start = num.popleft()
        
        # 시작 값을 deuqe에 넣어줌 
        q = deque() 
        q.append(start)
        q.append(-start)
        
        # bfs 탐색 시작 : 부분 누적 합에 새로운 값을 추가 
        while num:
            new = num.popleft()
            
            for _ in range(len(q)): 
                local_sum = q.popleft()
                q.append(local_sum + new)
                q.append(local_sum - new)
        
        # 최종 누적 합에서 찾는 숫자의 개수 세기
        return q.count(target)
    
    return num_bfs(numbers)
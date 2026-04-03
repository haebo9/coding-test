def solution(diffs, times, limit):
    def cal(lv): 
        "특정 숙련도에서 성공 실패 유무 계산"
        total = 0
        for i in range(len(diffs)): 
            if diffs[i] <= lv: 
                total += times[i]
            else: 
                # i == 0이면 이전 문제 계산 없음 
                if i >= 1: 
                    total += (times[i-1] + times[i])*(diffs[i]-lv) + times[i] 
                else: 
                    total += (times[i])*(diffs[i]-lv) + times[i] 
            if total > limit: 
                return False
            
        return total <= limit
        
    start = 1 # 숙련도 최솟값은 1
    end = max(diffs)
    answer = end
    
    while start <= end:  
        # 중간 위치 (타겟)
        mid = ( start + end ) // 2
        # print(mid)
        
        # 현재 위치 성공 -> 더 작은 값도 가능한지 확인
        if cal(mid): 
            answer = mid # 일단 성공 기록
            end = mid-1
            
        # 현재 위치 실패 -> 큰값 확인
        else: 
            start = mid+1
    
    return answer 

        
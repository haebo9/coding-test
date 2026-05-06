def solution(signals):
    """
    신호등 신호 : 초->노->빨 
    모든 신호등이 노란색이면 정전 -> 가장 빠른 시각 리턴 (없으면 -1)
    
    전략 : 각 신호등의 노란불인 시간을 담은 집합 들의 교집합 중 최솟값 출력 
    - 노란불 시작 시간 : 초 + 1
    - 두번째 노란불 시간 : 초 + 노 + 빨  / + 초 + 1
    - 세번째 노란불 시간 : 초 + 노 + 빨 + /  초 + 노 + 빨  / + 초 + 1
    """
    answer = set()
    start = True
    
    for sig in signals: 
        temp = set()
        g, y, r = sig
        
        for i in range(100000): 
            for k in range(y): 
                temp.add((g+y+r)*i + g+1 + k) 
                
        if start: 
            answer = temp 
            start = False
        else: 
            answer = temp & answer 
            
    return (min(answer) if answer else -1)
                
    # return answer
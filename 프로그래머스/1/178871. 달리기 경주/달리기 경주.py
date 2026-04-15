def solution(players, callings):
    # 각 선수의 시작 위치를 담은 딕셔너리 
    numbers = {p:i for i, p in enumerate(players)}
    
    for c in callings: 
        # 이름 불린 선수의 위치
        idx = numbers[c]
        prev = players[idx-1]
        
        # 앞선수와 위치 교환 
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        # 딕셔너리의 위치값 수정 
        numbers[prev] += 1
        numbers[c] -= 1
    
    return players
        
        
        
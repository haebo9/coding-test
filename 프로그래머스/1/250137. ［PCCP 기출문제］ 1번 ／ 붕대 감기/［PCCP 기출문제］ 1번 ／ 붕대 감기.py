def solution(bandage, health, attacks):
    # 붕대감기는 계속해서 시도하여 t초 연속이 될때 마다 체력을 회복 (최대 체력 이하)
    # 공격은 빠른 시간 순서대로 들어오는데 공격이 되면 체력이 감소하고 붕대감기도 취소
    # 체력이 0이 되는 것과 공격이 끝나는 것 중 어떤 것이 우세할지를 계산하는 것 
    "전략: 공격 시간을 하나씩 읽어가며 공격이 될 떄까지 몇번의 회복이 가능한지 계산 후 체력 증가 + 공격 후 체력 계산"
    
    curr = 0 # 현재 시간 
    t, x, y = bandage # t(시전시간), x(초당 회복량), y(추가 회복량)
    h = health # 현재 체력 
    
    for time, damage in attacks: 
        # 새로운 공격이 진행되기 까지의 시간 계산 
        duration = time - curr -1 
        
        # 공격 전 증가된 체력
        if duration > 0: 
            up = x*duration + y*(duration//t)
            h = min(health, up+h) # 최대체력 이하

        # 공격 후 체력
        h -= damage
        if h <= 0: 
            return -1
        
        # 시간 갱신 
        curr = time 
    
    return h
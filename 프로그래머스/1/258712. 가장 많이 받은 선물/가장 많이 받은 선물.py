def solution(friends, gifts):
    # 선물 받는 경우
        # 둘 중에서 많이 준 사람이 받음 
        # 같다면 선물 지수 높은 사람이 받음 
    # 두 사람간 비교 표가 있으면 좋을 것 같음 (횟수, 지수)
        # 딕셔너리 안에 리스트로 처리 
        
    give_take = {i : {} for i in friends}
    result = {i : 0 for i in friends}
    same_check = set()
    
    for i in gifts:
        g, t = i.split()
        try :
            give_take[g][t] += 1
        except : 
            give_take[g][t] = 1
    
    
    for gk, gv in give_take.items():
        for tk, tv in give_take.items():
            if frozenset({tk,gk}) in same_check: 
                pass
            else:
                same_check.add(frozenset({tk,gk}))
                
                if give_take[tk].get(gk,0) < give_take[gk].get(tk,0) : # tk 한테 받은거 보다 준게 많으면
                    result[gk] += 1
                elif give_take[tk].get(gk,0) > give_take[gk].get(tk, 0):
                    result[tk] += 1
                else: 
                    gk_take_total = sum([val.get(gk,0) for val in give_take.values()])
                    gk_give_total = sum(give_take[gk].values())
                    gk_index = gk_give_total - gk_take_total

                    tk_take_total = sum([val.get(tk,0) for val in give_take.values()])
                    tk_give_total = sum(give_take[tk].values())
                    tk_index = tk_give_total - tk_take_total

                    if (gk_index < tk_index): 
                        result[tk] += 1
                    elif (gk_index > tk_index): 
                        result[gk] += 1
                    else: 
                        pass
        
    print(give_take)
    print(result)

    return max(result.values())

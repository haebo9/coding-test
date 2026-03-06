from collections import Counter

def solution(topping):
    answer = 0
    p1 = dict(Counter(topping))
    p2 = set()

    for t in topping: 
        p2.add(t)  
        if t in p1:
            p1[t] -= 1
        
            if p1[t] == 0: 
                del p1[t]
        
            if len(p1) == len(p2): 
                answer +=1

    return answer
import sys
input = sys.stdin.readline 

n, new, p = map(int, input().strip().split())
scores = list(map(int, input().strip().split()))

def solution(n, new, p, scores): 
    if n and new <= scores[-1]: 
        if len(scores) < p:
            scores.append(new)
        else: 
            return -1  

    result = 0
    for i in scores: 
        if i > new: 
            result += 1
        elif i < new: 
            return result + 1
    return result + 1

print(solution(n, new, p, scores))
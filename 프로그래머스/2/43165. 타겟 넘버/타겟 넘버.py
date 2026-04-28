def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def backtrack(idx, total): 
        nonlocal n, answer
        if idx == n: 
            if total == target: 
                answer += 1
            return 
            
        for num in (numbers[idx], -numbers[idx]): 
            backtrack(idx+1, total+num)
    
    backtrack(idx=0, total=0)
    
    return answer
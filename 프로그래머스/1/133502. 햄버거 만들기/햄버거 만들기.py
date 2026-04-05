def solution(ingredient):
    answer = 0
    stack = []
    for i in range(len(ingredient)): 
        # 재료 하나씩 추가
        stack.append(ingredient[i])
        # 햄버거 만들수 있는지 확인
        if len(stack) >= 4   and stack[-4:] == [1,2,3,1]: 
            print('-', stack[-4:])
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1
            
    return answer
def solution(word):
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [] 
    
    def backtrack(curr_word): 
        # 길이 5 넘어가면 종료 
        if len(curr_word) > 5: 
            return 
        
        # 단어가 생길 때 마다 결과에 저장 
        if curr_word: 
            result.append(curr_word)
        
        # 모음에 대해 현재 단어에 하나씩 추가하는 로직(백트랙킹)
        for v in vowels: 
            backtrack(curr_word + v)
    
    # 공백을 시작으로 백트랙킹 탐색 시작 
    backtrack(curr_word='')    
    result = sorted(result) # 사전순 정렬 
    return (result.index(word) + 1) # 찾는 값이 몇번쨰인지 확인 (index +1)
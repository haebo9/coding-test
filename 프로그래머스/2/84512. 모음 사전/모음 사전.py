from itertools import product
def solution(word):
    
    # 사용할 수 있는 알파벳 후보 (빈칸 포함))
    alp = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    # 1. 1글자부터 5글자까지 모든 조합 생성
    for i in range(1, 6):
        for p in product(alp, repeat=i):
            # p는 ('A', 'E') 같은 튜플 형태이므로 문자열로 합쳐줌
            words.append("".join(p))
    
    sorted_word = sorted(words)
    return sorted_word.index(word)+1
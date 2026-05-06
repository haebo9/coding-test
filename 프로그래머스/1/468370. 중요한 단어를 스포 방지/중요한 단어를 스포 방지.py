from collections import Counter

def solution(message, spoiler_ranges):
    # 구간 배열이 이미 오름차순이므로 정렬 생략
    
    w_lst = message.split()
    if not w_lst: return 0
    
    w_dict = Counter(w_lst)
    spoiler = set()
    
    wi = 0 
    chk = 1 # 1: 검사 필요, 0: 현재 단어 완료
    sri = 0 
    
    for i, m in enumerate(message):
        if m == ' ':
            wi += 1
            chk = 1
            continue
        
        # 이미 이 단어를 스포일러로 처리했다면 다음 글자들은 무시
        if not chk:
            continue
            
        # wi가 범위를 벗어나는 것을 방지 (문자열 끝 공백 등 예외 상황 대비)
        if wi >= len(w_lst):
            break

        # 현재 인덱스 i가 스포일러 구간에 속하는지 확인
        for sr in range(sri, len(spoiler_ranges)):
            s, e = spoiler_ranges[sr]

            if i < s: # 현재 위치가 구간 시작점보다 앞서면 종료
                break

            if s <= i <= e:
                w = w_lst[wi]
                spoiler.add(w)
                w_dict[w] -= 1
                chk = 0
                sri = sr # 현재 구간부터 다음 탐색 시작
                break

            if i > e: # 이미 지나친 구간은 다음 탐색에서 제외
                sri = sr + 1
    
    answer = 0
    for sp in spoiler:
        if w_dict[sp] == 0:
            answer += 1
            
    return answer
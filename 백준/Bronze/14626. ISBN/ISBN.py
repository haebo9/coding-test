def isbn(nums): 
    """
    훼손된 자리의 숫자를 찾아내는 함수

    - idx 짝수는 가중치 1, 홀수는 가중치 3
    - idx 0~11까지의 숫자, 12는 체크 기호
    """
    total = 0
    chk = -1
    m = int(nums[-1])

    for i,x in enumerate(nums): 
        if i < 12: 
            # 훼손된 숫자가 아닐떄
            if x != '*': 
                total += int(x)*(1 if i%2==0 else 3)
            
            # 훼손된 숫자일떄 
            else: 
                chk = (1 if i%2==0 else 3)
        
        # 마지막 번호 m은 가중치 없이 더해줌
        else: 
            total += int(x)
    
    # 훼손된 숫자 찾기 
    for i in range(0, 9+1): 
        if ( total + chk*i ) % 10 == 0: 
            return i

import sys
input = sys.stdin.readline 

nums = input().strip()
print(isbn(nums))
def quad_tree(x, y, add): 
    "같은 숫자끼리 있으면 뭉쳐서 표현하는 함수. 4등분 단위로 묶음"
    # 같은 값으로 되었는지 확인
    color = nums[x][y]

    for i in range(x, x+add): 
        for j in range(y, y+add): 
            if nums[i][j] != color: 
                # 영역 4등분
                q_add = add//2

                part1 = quad_tree(x, y, q_add) # 왼쪽 위
                part2 = quad_tree(x, y+q_add, q_add) # 오른쪽 위
                part3 = quad_tree(x+q_add, y, q_add) # 왼쪽 아래
                part4 = quad_tree(x+q_add, y+q_add, q_add) # 오른쪽 아래 
                
                # 하나라도 다른게 섞였고, 4등분도 완료했으면 반환 
                return f'({part1}{part2}{part3}{part4})'
    
    return color

import sys
input = sys.stdin.readline 

n = int(input())
nums = [list(input().strip()) for _ in range(n)] 

print(quad_tree(x=0, y=0, add=n))
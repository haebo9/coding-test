def paper_devide(x, y, size):  
    global result, n, paper
    """ 
    동일한 숫자로 이루어진 종이의 수를 구하는 함수
    
    Args
    x : 영역의 시작하는 좌표의 row값
    y : 영역의 시작하는 좌표의 col값
    size : 영역 내 종이의 길이 (한칸이 1)
    """
    # 첫번째 값의 숫자 확인 
    chk = paper[x][y] 

    # 영역 내 모든 수가 동일한 수인지 확인 
    for i in range(x, x+size): 
        for j in range(y, y+size): 
            if paper[i][j] != chk: 
                # 만약에 하나라도 다른 숫자가 있다면 가로세로 3등분 (9등분)
                new = size // 3
                parts = [(x, y, new), (x, y+new, new), (x, y+2*new, new), 
                         (x+new, y, new), (x+new, y+new, new), (x+new, y+2*new, new), 
                         (x+2*new, y, new), (x+2*new, y+new, new), (x+2*new, y+2*new, new)]
                for p in parts: 
                    paper_devide(p[0], p[1], p[2])

                # 다른 값이 섞여서 분할을 완료했다면 해당 반복은 종료 
                return 
    # 만약에 영역이 하나의 숫자로 되어 있다면
    result[chk] += 1

# 함수 실행 
import sys
input = sys.stdin.readline 

n = int(input())
result = {-1:0, 0:0, 1:0}
paper = [list(map(int, input().strip().split())) for _ in range(n)]
paper_devide(x=0, y=0, size=n) 

# 정답 출력
print(result[-1])
print(result[0])
print(result[1])
import sys
input = sys.stdin.readline

wait_line = [] # 예비 공간 

# line에서 1번 부터 차례대로 나가면 됨
n = int(input())
line = list(map(int, input().strip().split())) # 초기 대기줄
line = line[::-1] # 맨 앞의 수가 제일 먼저 나갈수 있도록 

def chech_wait_line():
    global wait_line, target
    while wait_line: 
        if wait_line[-1] == target:
            wait_line.pop()
            target +=1 
        else: 
            break

target = 1
for i in range(1, n+1): 
    # print(target)

    # 타겟이 아니면 대기줄에 추가
    if line[-1] != target: 
        chech_wait_line()
        temp = line.pop()
        wait_line.append(temp)
        
    # 타깃이면 제거 
    else:
        line.pop()
        target += 1 
        chech_wait_line()


print('Nice' if not wait_line else 'Sad')
    
# print(line)
# print(wait_line)
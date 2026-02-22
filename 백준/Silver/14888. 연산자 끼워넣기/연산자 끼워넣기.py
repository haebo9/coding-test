# 사칙연산의 연산자(+, -, x, %) 가능 개수가 주어짐. : 동일한 계산을 반복할 필요는 없음. 
# 앞에서부터 모든 연산자에 대해 반복하되, 가능한 연산자 수를 고려해야 함. 
# 최종 값을 최댓값과 최솟값과 비교 갱신을 진행함. 

def cal(result, num, f:int): 
    if f == 0:
        return result + num
    elif f == 1: 
        return result - num 
    elif f == 2: 
        return result * num 
    elif f == 3: 
        return int(result / num)

def backtrack(index, result): 
    """ 앞에서 부터 가능한 연산을 진행 """
    global n, r_max, r_min, n, func

    if index == n:
        if result > r_max: 
            r_max = result
        if result < r_min:
            r_min = result  
        return 

    for f in range(4): # +, -, x, %
        if func[f] > 0: 
            func[f] -= 1
            
            # 다음 result 계산을 인자로 바로 넣는 방식을 사용 : 이전의 result 값 보존
            backtrack(index+1, cal(result, num[index], f)) 
            
            func[f] += 1

# import sys
# input = sys.stdin.readline

n = int(input())
num = list(map(int, input().strip().split()))
func = list(map(int, input().strip().split())) # +, -, x, %

r_max = float('-inf')
r_min = float('inf')

backtrack(index=1, result=num[0])

print(r_max) 
print(r_min)
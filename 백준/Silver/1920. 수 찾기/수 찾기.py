import sys 
input = sys.stdin.readline

n = int(input())
n_array = list(map(int, input().strip().split()))
n_array = sorted(n_array)

m = int(input())
m_array = list(map(int, input().strip().split()))

def solutions(target):
    global n_array

    start = 0
    end = len(n_array)-1

    while start <= end: 
        mid = (start+end) //2

        # 중간보다 크기에 중간 다음부터 확인
        if target > n_array[mid]: 
            start = mid + 1 
        
        # 중간보다 작기에 중간 이전까지 확인
        elif target < n_array[mid]: 
            end = mid -1 

        # 일치했을 때 
        else:
            return 1
    
    return 0

for target in m_array: 
    print(solutions(target))
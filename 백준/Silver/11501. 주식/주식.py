import sys
input = sys.stdin.readline 

def stock(n, prices): 
    "일별 가격 배열을 받아서 최대 이익을 계산 : 뒤에 더 큰값이 있으면 사는게 이득, 제일 비쌀때 판매" 

    # 각 위치에서 가장 높은 값을 찾음 
    result = 0
    curr = prices[-1]

    for i in range(n-1, -1, -1): 
        if prices[i] > curr: 
            curr = prices[i]

        # 현재 위치에서 최고값보다 큰 값인 경우 수익에 추가 
        temp = curr - prices[i]
        if temp > 0: 
            result += temp 
    
    return result

for _ in range(int(input())):
    n = int(input())
    prices = list(map(int, input().strip().split()))
    print(stock(n, prices))
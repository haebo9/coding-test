# 왼쪽 -> 오른쪽 최소비용으로 이동 : n = 10^5
# 제일 싸게 가는 방법 : 비싸면 최소한으로, 싸면 최대한으로 기름을 넣으면 될 듯 ! 
    # 앞에부터 최소한으로 구매하는데, 다음으로 싼 곳이 나올 때까지만 갈수있는 기름 충전 
    # 다음 구매지 까지 몇칸인지를 계산해내야 함 
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().strip().split()))
price = list(map(int, input().strip().split()))

len_price = len(price)
total_price = 0 
curr_price = price[0]

i = 0 # 현재 위치
while i < len_price-1 : 
    cnt = 0 # 몇칸 가야하는지 계산 
    for j in range(i+1, len_price):
        cnt += 1
        if price[j] < curr_price:
            new_price = price[j]
            break
        else: 
            new_price = curr_price

    # print((i, j), cnt)
    while cnt > 0: 
        # 앞으로 1칸씩 이동 로직 
        cnt -= 1
        i += 1
        dict_i = i-1 # i 번째 주유소로 갈때의 거리 
        total_price += curr_price*dist[dict_i]
    else: 
        curr_price = new_price
        # print(i)

print(total_price) 
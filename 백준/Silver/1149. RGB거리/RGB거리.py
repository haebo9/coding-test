# DP 
# 1번 집부터 R,G,B를 칠했을때의 최솟값을 각각 갱신하면서 진행
# import sys
# input = sys.stdin.readline

n = int(input()) 
house = [list(map(int, input().strip().split())) for _ in range(n)]

for i in range(1, n): 
    # i번째 집을 r로 칠하는 최솟비용 = i-1번째 집이 g 또는 b일때의 최소 비용과 r로 칠하는 비용의 합
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])

# r,g,b의 최소비용 중 최소인 값을 선택
result = min(house[-1])
print(result)
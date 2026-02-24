# i번쨰 줄에서 각 숫자는 선택할수 있는 i-1숫자 중에  가장 큰것을 골라서 합을 자신의 자리에 넣는다. 
# i번째 줄의 k번째 값이 선택할 수 있는 다음 숫자는 i+1번째 줄의 k, k+1 번 수이다. 
# = i번째 줄의 k 번값을 선택할수 있는 i-1번째 줄의 수는 k-1, k번 값임
import sys
input = sys.stdin.readline 

n = int(input())
nums = [list(map(int, input().strip().split())) for _ in range(n)]
# nums = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(1, n): 
    for k, num in enumerate(nums[i]):
        if 0 < k and k < i: # 중간
            nums[i][k] += max(nums[i-1][k-1], nums[i-1][k])
        elif k ==0: # 죄측 끝
            nums[i][k] += nums[i-1][k]
        elif k == i: # 우측 끝
            nums[i][k] += nums[i-1][k-1]

print(max(nums[-1]))
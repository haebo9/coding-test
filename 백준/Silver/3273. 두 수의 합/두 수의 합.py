import sys
input = sys.stdin.readline 
# 투 포인터 
# i, j에서의 합이 x보다 작으면 s+1 / 크거나 같으면 e-1
# 1 <= i < j <= n

n = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()
x = int(input())

s = 0
e = n-1
result = 0

while s < e: 
    total = arr[s] + arr[e]
    
    # 합이 x와 같으면 결과 + 1 / 다음으로 이동 
    if total == x: 
        result += 1
        s += 1
        e -= 1

    # 합이 x보다 작으면 e 증가, 크면 s 증가
    elif total < x:
        s += 1
    else: 
        e -= 1

print(result) 
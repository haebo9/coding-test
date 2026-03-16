# 사람과 K거리의(차이가 2) 햄버거를 먹을 수 있음 
# 좌측 먼저, 우측 다음으로 확인 
# 사람과 햄버거의 위치를 따로 추출해서 한명씩 버거 할당 
import sys
input = sys.stdin.readline 

n, k = map(int, input().strip().split())
arr = input().strip()

def solution(n, k, arr): 
    hi = []
    pi = []

    for i, a in enumerate(arr): 
        if a == 'H': 
            hi.append(i)
        else: 
            pi.append(i)

    # print(hi, pi)

    answer = 0 
    visited = set()

    i = 0
    saved_i = i

    for p in pi: 
        i = saved_i
        while i < len(hi): 
            if (i not in visited) and (abs(p-hi[i]) <= k) : 
                # print(p, hi[i])
                visited.add(i)
                saved_i = i+1
                answer += 1
                break

            elif (i not in visited) and (k < hi[i]-p): 
                break 

            else: 
                i += 1
     
    return answer

print(solution(n, k, arr))
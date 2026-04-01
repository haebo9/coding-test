from collections import deque 
import sys
input = sys.stdin.readline 

def bfs(lst): 
    # 보드판 
    visited = [[0]*10 for _ in range(10)] 
     
    # 시작 위치 설정 
    q = deque([1])

    while q: 
        num = q.popleft()
        r, c = divmod(num-1, 10)

        if num == 100: 
            return visited[r][c]

        # 뱀 or 사다리 
        if lst[num]: 
            num = lst[num][0]
            nr, nc = divmod(num-1, 10)
            visited[nr][nc] = visited[r][c]

        # 주사위 쿨리기
        for i in range(1, 6+1): 
            if num+i <= 100: 
                nr, nc = divmod(num+i-1, 10)
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] +1
                    q.append(num+i)

n, m = map(int, input().split())

lst = [[] for _ in range(101)] # 1~100번 칸 
for _ in range(n+m):
    u, v = map(int, input().split())
    lst[u].append(v)

result = bfs(lst)
print(result)
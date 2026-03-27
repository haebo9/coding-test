from collections import deque
import sys
input = sys.stdin.readline 

def bfs(l, start, end): 
    visited = [[0]*l for _ in range(l)]
    q = deque()
    q.append(start)

    if start == end: 
        return 0

    while q: 
        r, c = q.popleft()
        cnt = visited[r][c]

        for dr, dc in [(1, -2), (2, -1), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)] : 
            nr = r + dr
            nc = c + dc
            if 0 <= nr < l and 0 <= nc < l and not visited[nr][nc]: 
                if nr == end[0] and nc == end[1]: 
                    return cnt + 1

                visited[nr][nc] = cnt + 1
                q.append((nr, nc))

t = int(input())
for _ in range(t): 
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    print(bfs(l, start, end))
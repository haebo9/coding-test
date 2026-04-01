def dfs(u, team): # u -> v
    "그래프 연결 엣지를 따라 탐색"
    global visited, linked, result 

    visited[u] = team
    
    for v in linked[u]:  
        # 가는 곳이 처음 방문하는 경우 
        if visited[v] == '': 
            # 방문할 곳에 반대 색을 전달 + False 반환시 리턴 False
            if not dfs(v, 'B' if team =='A' else 'A'): 
                return False
        # 이미 방문한 적 있는 경우 + 팀도 같은 경우 
        elif visited[v] == team: 
            return False
    
    return True

import sys
input = sys.stdin.readline 
sys.setrecursionlimit(200000)

for _ in range(int(input())):
    # 입력 
    V, E = map(int, input().split()) # 노드/엣지의 개수
    linked = [[] for _ in range(V+1)]
    
    for _ in range(E): 
        u, v = map(int, input().split())
        linked[u].append(v)
        linked[v].append(u)

    # 방문 기록
    visited = ['']*(V+1)
    result = 'YES'

    # 결과
    for i in range(1, V+1): 
        if visited[i]=='': 
            if not dfs(u=i, team='A'): 
                result = 'NO'
                break 

    print(result) 
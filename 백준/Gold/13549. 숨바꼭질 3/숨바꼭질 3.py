import heapq
import sys
input = sys.stdin.readline 

def bfs(n, k): 
    """
    전략: 수빈이의 위치에서 즉시 가능한 모든 순간이동을 수행하고, 1초 후 위치 이동을 수행한다.
    
    알고리즘 : 다익스트라 (heapq) - 특정 위치에서의 최단거리 보장 
    가중치가 0과 1로 이루어진 그래프 탐색
    """
    q = [] 
    heapq.heappush(q, (1, n)) # (w, n): w는 진행된 시간, n은 현재 위치
    
    visited = [float('inf')]*100001 # 방문 처리 

    while q: 
        w, x= heapq.heappop(q) # x에서의 최단시간
        visited[x] = w 

        if x == k: # 목적지 도착 
            return w-1 # 시작 시간 1 -> 0으로 값 보정 
        
        for mv in [x*2]: 
            if 0<= mv <= 100000:
                if w < visited[mv]: 
                    heapq.heappush(q, (w, mv))

        for mv in [x-1, x+1]: 
            if 0<= mv <= 100000:
                if w+1 < visited[mv]: 
                    heapq.heappush(q, (w+1, mv))

n, k = map(int, input().split())
print(bfs(n, k))
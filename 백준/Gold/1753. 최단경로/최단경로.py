import heapq
import sys
input = sys.stdin.readline 

def dijkstra(V, K, edges): 

    dist = [float('inf')]*(V+1) # 모든 노드로의 최단 거리는 무한대로 초기화 
    q = []

    heapq.heappush(q, (0, K))
    dist[K] = 0

    while q: 
        # 누적 거리 합이 가장 짧은 노드 꺼내기 (특정 노드 까지의 최단 거리임을 보장)
        d, u = heapq.heappop(q)

        for v, w in edges[u]: 
            new_d = d + w # u -> v의 누적 가중치 
            # v의 최단 경로보다 작은 경우 갱신 + 큐에 추가
            if new_d < dist[v]: 
                dist[v] = new_d
                heapq.heappush(q, (new_d, v))
    
    dist = ['INF' if i == float('inf') else i for i in dist[1:]]
    return dist

# 입력값 
V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(V+1)]

for _ in range(E): 
    u, v, w = map(int, input().split())
    edges[u].append((v, w)) # 최소 힙을 위해 가중치를 앞으로

# 탐색 결과 출력
result = dijkstra(V, K, edges)
print(*result, sep='\n')
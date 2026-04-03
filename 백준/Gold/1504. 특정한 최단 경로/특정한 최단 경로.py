from heapq import heappush, heappop
import sys
input = sys.stdin.readline 

def dijkstra(start, end): 
    "다익스트라 알고리즘 사용 : start -> end 최단 경로 계산"
    global edges

    q = []
    totals = [float('inf')]*(N+1)
    totals[start] = 0

    # 시작 위치에서의 total값과 노드 추가
    heappush(q, (0, start))

    while q:
        # start -> a 경로의 최단 경로임을 보장  
        # a -> b 경로의 거리는 c (edges 배열 내 값 - (b, c))
        total, a = heappop(q)
        if totals[a] < total: 
            continue

        for b, c in edges[a]:
            if totals[b] > totals[a] + c:
                totals[b] = totals[a] + c
                heappush(q, (totals[a] + c, b)) 
    
    # print(start, end, totals, totals[end])
    return totals[end]

# 입력값 
N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(E): 
    a, b, c = map(int, input().split())
    # 양방향 그래프(주의 !)
    edges[a].append((b,c))
    edges[b].append((a,c))

v1, v2 = map(int, input().split())

# 정답 후보1 : 1 -> v1 -> v2 -> N
result1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
# 정답 후보2 : 1 -> v2 -> v1 -> N
result2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

result = min(result1, result2) # 작은 값
print(-1 if result == float('inf') else result) # 경로 없는 지 확인
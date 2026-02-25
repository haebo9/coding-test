import sys
input = sys.stdin.readline 

# 1번과 연결되어 있는 모든 컴퓨터 개수를 찾는 문제 
# 딕셔너리로 각 번호에 연결된 컴퓨터를 리스트 형태로 넣는다. 
# 그리고 1번부터 이동하며 찾은 컴퓨터는 집합에 저장해두고 못찾은 컴퓨터 위주로 탐색한다. 

n = int(input()) # 컴퓨터 개수
m = int(input()) # 연결 개수

# 연결 정보를 담은 딕셔너리 
link = {i : [] for i in range(1, n+1)}
for _ in range(m): 
    a, b = map(int, input().strip().split())
    link[a].append(b)
    link[b].append(a) 

target = link[1]
visited = set([1])

while target: 
    # 1에 연결된 타겟 하나 탐색
    t = target.pop()

    # 이전에 탐색하지 않았다면
    if t not in visited: 
        visited.add(t)
        # target에 연결된 컴퓨터 탐색
        for next in link[t]: 
            target.append(next)

# 1을 제외한 연결됨 컴퓨터 수
print(len(visited)-1)
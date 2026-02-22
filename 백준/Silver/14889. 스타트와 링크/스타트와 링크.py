from itertools import combinations

def comb_dic(n): 
    all = set(range(n))
    
    team1 = list(combinations(all, n//2))
    team2 = []
    for t in team1: 
        team2.append(tuple(all - set(t)))
    
    return team1, team2

def score(t1, t2): 
    global smap
    score1, score2 = 0, 0
    
    for i in list(combinations(t1, 2)):
        a, b = i[0], i[1]
        score1 += smap[a][b] + smap[b][a]

    for j in list(combinations(t2, 2)):
        a, b = j[0], j[1]
        score2 += smap[a][b] + smap[b][a]
    
    return abs(score1 - score2)

import sys
input = sys.stdin.readline 
n = int(input())
smap = [list(map(int, input().strip().split())) for _ in range(n)]
# smap = [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
# smap = [[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5], [1, 2, 3, 0, 4, 5], [1, 2, 3, 4, 0, 5], [1, 2, 3, 4, 5, 0]]

team1, team2 = comb_dic(n)

# print(team1)
# print(team2)

result = float('inf')
for t1, t2 in zip(team1, team2):
    diff = score(t1, t2)
    if diff < result: 
        result = diff

print(result) 
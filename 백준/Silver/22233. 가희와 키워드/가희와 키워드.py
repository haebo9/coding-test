import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
keyword = set()

for _ in range(n): 
    keyword.add(input().strip())    

for _ in range(m): 
    for k in input().strip().split(','):
        keyword.discard(k)
    print(len(keyword))
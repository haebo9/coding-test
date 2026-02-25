import sys
input = sys.stdin.readline 

n, m = map(int, input().strip().split())
sites = {} 
for _ in range(n): 
    site, pw = input().strip().split()
    sites[site] = pw

for _ in range(m): 
    site = input().strip()
    print(sites[site])
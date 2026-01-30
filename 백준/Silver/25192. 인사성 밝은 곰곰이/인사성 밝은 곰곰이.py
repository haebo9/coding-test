import sys 
input = sys.stdin.readline

n = int(input())

record = set()
cnt = 0 

for _ in range(n):
    text = input().strip()
    if text == "ENTER": 
        cnt += len(record)
        record = set()
    else: 
        record.add(text)

cnt += len(record)

print(cnt) 
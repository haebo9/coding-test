import sys
input = sys.stdin.readline 

member = set()

for _ in range(int(input())):
    name, el = input().strip().split()
    if el == 'enter': 
        member.add(name)
    else: # leave
        member.discard(name)

result = sorted(member, reverse=True) 
print(*result, sep='\n')
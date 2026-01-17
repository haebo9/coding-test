def check(user):
    used = []
    temp = str
    for i in user:
        if i in used:
            return False
        else: 
            if i == temp:
                temp = i
            else: 
                used.append(temp)
                temp = i
    else: 
        return True

import sys 
n = int(sys.stdin.readline().strip())
answer = 0

for _ in range(n): 
    user = sys.stdin.readline().strip()
    answer += int(check(user))

print(answer)
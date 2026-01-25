import sys
input = sys.stdin.readline

def check_vps(data:str)->bool:
    stack = []
    for i in data:
        if i == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    else:
        if not stack: # 비어있으면
            return True
        else: # 안비어있으면
            return False

for _ in range(int(input().strip())):
    user = input().strip()
    if check_vps(user):
        print('YES')
    else:
        print('NO')
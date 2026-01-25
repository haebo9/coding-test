import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    num = input().strip()

    if len(num) > 1: 
        num, x = map(int, num.split())
        stack.append(x)
    
    else: 
        num = int(num)
        if num ==2: 
            print(stack.pop() if stack else -1)
        elif num ==3: 
            print(len(stack))
        elif num ==4: 
            print(1 if not stack else 0) 
        elif num ==5:
            print(stack[-1] if stack else -1)
        else: 
            print('error')
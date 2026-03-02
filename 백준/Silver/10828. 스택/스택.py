def push(x): 
    global stack
    stack.append(x)

def pop(): 
    global stack
    print(stack.pop() if stack else -1)

def size(): 
    global stack
    print(len(stack))

def empty(): 
    global stack
    print(0 if stack else 1) 

def top(): 
    global stack
    print(stack[-1] if stack else -1) 

import sys
input = sys.stdin.readline 

stack = []
func = {"push":push, "pop":pop, "size":size, "empty":empty, "top":top}

n = int(input().strip())
for _ in range(n): 
    f, *x = input().strip().split()
    func[f](*x)
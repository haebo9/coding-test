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

stack = []
func = {"push":push, "pop":pop, "size":size, "empty":empty, "top":top}

n = int(sys.stdin.readline())
for line in sys.stdin: 
    f, *x = line.strip().split()
    func[f](*x)
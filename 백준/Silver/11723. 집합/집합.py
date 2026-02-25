class Process: 
    def __init__(self): 
        self.s = set()

    def add(self, x):
        if x not in self.s:
            self.s.add(x)

    def remove(self, x): 
        if x in self.s: 
            self.s.remove(x)

    def check(self, x): 
        if x in self.s: 
            print(1)
        else: 
            print(0)
    
    def toggle(self, x): 
        if x in self.s: 
            self.s.remove(x)
        else: 
            self.s.add(x)
    
    def all(self): 
        self.s = set(range(1, 21))
    
    def empty(self): 
        self.s = set()


import sys
input = sys.stdin.readline 

process = Process()
f_map = {'add':process.add, 'remove':process.remove,'check':process.check,
         'toggle':process.toggle, 'all':process.all, 'empty':process.empty}

for _ in range(int(input())): 
    order, *x = input().strip().split()
    if x: 
        f_map[order](int(x[0]))
    else : 
        f_map[order]()
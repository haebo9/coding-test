def triangle(a,b,c): 
    if b+c > a: 
        temp = len(set([a,b,c]))
        map = {1:'Equilateral',2: 'Isosceles',3: 'Scalene'}
        print(map[temp]) 
    else: 
        print('Invalid')

import sys
input = sys.stdin.readline 

while True: 
    nums = list(map(int, input().strip().split()))
    a,b,c = sorted(nums, reverse=True)
    if a==b==c==0: 
        break
    triangle(a,b,c)
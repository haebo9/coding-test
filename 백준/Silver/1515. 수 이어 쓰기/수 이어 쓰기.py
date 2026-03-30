import sys
input = sys.stdin.readline 

def solution(num, l):
    idx = 0 
    i = 0
    while True: 
        i += 1
        for t in str(i):     
            if num[idx] == t: 
                idx += 1
                if idx == l: 
                    return int(i)
            else: 
                continue
            
num = input().strip()
l = len(num)

print(solution(num, l))
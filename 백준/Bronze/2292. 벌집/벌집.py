# 1층 : 1 
# 2층 : 2~7 + 6
# 3층 : 8~19 + 12
# 4층 : 20~37 + 18
# 5층 : 38~61 + 24
# 6층  : 62~91 + 30 
# 7층 : 92~ .. 

# K층 시작 값 = 1 + 1 + 6*1 + 6*2 + ... 6*(K-1) = 2 + 6*(K*(K-1)/2)

def layer(n):
    start = 2
    check = 2
    while True: 
        if n >= start: 
            start += 6*(check-1)
            check += 1
        else: 
            return check-1

n = int(input())
print(layer(n))
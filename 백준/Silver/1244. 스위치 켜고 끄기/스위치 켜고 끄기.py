import sys
input = sys.stdin.readline 

def change(i): 
    global switch
    if switch[i] == 1: 
        switch[i] = 0
    else:
        switch[i] = 1 

def order(sex, num): 
    global switch, n 
    if sex == 1: # 남자 
        for i in range(num, n+1 , num): 
            change(i)

    else: # 여자 
        change(num)
        i = 1
        while (1<= num-i and num + i <= n) and (switch[num-i] == switch[num+i]): 
            change(num-i)
            change(num+i)
            i += 1

n = int(input().strip())
switch = [-1] + list(map(int, input().strip().split()))
m = int(input().strip())

for _ in range(m): 
    sex, num = map(int, input().strip().split())
    order(sex, num)

for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:  # 20개 출력할 때마다 줄바꿈
        print()
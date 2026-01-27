import sys
input = sys.stdin.readline 

def check_perpect(num):
    temp = []
    for i in range(1, num//2+1):
        if num % i == 0: 
            temp.append(i)
    if num == sum(temp): 
        return f"{num} = {' + '.join(map(str, temp))}"
    else: 
        return f'{num} is NOT perfect.'

while True: 
    num = int(input().strip())
    if num == -1 : 
        break 
    else: 
        print(check_perpect(num))
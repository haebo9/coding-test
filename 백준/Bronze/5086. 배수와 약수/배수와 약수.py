import sys 
input = sys.stdin.readline

def check_num(num1, num2): 
    if num1 > num2 and num1%num2 ==0: 
        return 'multiple'
    elif num1 < num2 and num2%num1 ==0: 
        return 'factor' 
    else: 
        return 'neither'

num1, num2 = -1, -1
while True:
    num1, num2 = map(int, input().strip().split())
    if num1 == 0 and num2 == 0: 
        break
    else: 
        print(check_num(num1, num2))
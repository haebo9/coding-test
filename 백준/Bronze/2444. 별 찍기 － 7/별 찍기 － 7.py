n = int(input())

for i in range(1, n):
    temp = '*' * (2*i-1)
    emp = ' '*(((2*n-1) - (2*i-1))//2)
    print(emp+temp, end='\n')

print('*'*(2*n-1))

for i in range(n-1, 0, -1):
    temp = '*' * (2*i-1)
    emp = ' '*(((2*n-1) - (2*i-1))//2)
    print(emp+temp, end='\n')
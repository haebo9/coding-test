n = int(input())
lst = list(map(int, input().strip().split())) # a, b
curr = n

while curr:         
    if lst[0] >= 2: 
        lst[0] -= 2
    elif lst[1] >= 1:
        lst[1] -= 1
    else: 
        break 

    curr -= 1
print(n-curr)
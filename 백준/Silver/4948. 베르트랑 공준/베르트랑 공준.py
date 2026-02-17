# n보다 크고 2n보다 작거나 같은 소수의 개수
def decimal(n:int): 
    target = n + 1
    result = 0
    while target <= 2*n:
        if target > 2 and target % 2 == 0: 
            pass
        else:
            cond = (target if target <= 10 else int(target**0.5)+1)
            for i in range(3, cond, 2): 
                if target % i == 0: 
                    break
            else: 
                result += 1
    
        target += 1
    return result

while True: 
    n = int(input().strip())
    if n == 0: 
        break
    else:  
        print(decimal(n))
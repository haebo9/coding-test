def binomial(n, k): 
    if k == n or k == 0: 
        return 1
    if k == 1: 
        return n

    return binomial(n-1, k) + binomial(n-1, k-1)

n, k = map(int, input().strip().split())
print(binomial(n, k))
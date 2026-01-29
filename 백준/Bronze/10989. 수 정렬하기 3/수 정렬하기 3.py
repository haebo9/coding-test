import sys
input = sys.stdin.readline

dic = {}
n = int(input())

for _ in range(n):
    num = int(input())
    if num in dic.keys():
        dic[num] += 1
    else: 
        dic[num] = 1 

# print(dic)
cnt = 0

for i in iter(range(1, 10000+1)):
    try: 
        for _ in range(dic[i]):
            print(i)
            cnt +=1 
    except : 
        pass
    if cnt == n: 
        break
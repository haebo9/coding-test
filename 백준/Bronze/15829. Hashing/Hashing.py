import sys
input = sys.stdin.readline 

l = int(input())
num = [ord(s)-ord('a')+1 for s in input().strip()]
r = 31
m = 1234567891

# 수열 a : 알파벳(a~z)을 1~26으로 번호를 부여한 수열
def num_to_hash(l, num): 
    result = 0
    for i in range(0, l): 
        result += num[i] * (r**i) 
    return result % m

print(num_to_hash(l, num))
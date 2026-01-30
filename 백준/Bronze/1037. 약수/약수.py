# n % a = 0 
# n은 a의 배수 : a * k = n 
# n은 약수 중 가장 큰 수 * 가장 작은 수
import sys
input = sys.stdin.readline

cnt = int(input())
a_lst = list(map(int, input().strip().split()))

n = max(a_lst) * min(a_lst)
print(n)
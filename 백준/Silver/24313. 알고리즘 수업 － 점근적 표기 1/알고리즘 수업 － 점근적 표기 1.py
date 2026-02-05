"""
모든 n에 대하여 f(n) <= c * g(n)
f(n) = a1*n + a0 = 7n + 7
g(n) = n 

f(1) = 14
c* g(1) = 8

# 1. n0에서의 함숫값 조건: f(n0) <= c * g(n0)
# 2. 기울기 조건: a1 <= c (f의 기울기가 c*g의 기울기보다 작거나 같아야 함)
    -> a1 > c 면 나중에 더 커질 수 있음 (c는 g(n)의 기울기) 
""" 
import sys
input = sys.stdin.readline

a1, a0 = map(int, input().strip().split())
c = int(input())
n = int(input())

f = lambda n : a1*n + a0 
g = lambda n : n

if (f(n) <= c * g(n)) and (a1 <= c): 
    print(1) 
else: 
    print(0)
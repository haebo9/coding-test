a, b = map(int, input().split())
c, d = map(int, input().split())

def solution(a,b,c,d): 
    # 케이스 1: A의 오렌지를 옮기고 B의 사과를 옮김 (b + c)
    # 케이스 2: A의 사과를 옮기고 B의 오렌지를 옮김 (a + d)
    return min(b + c, a + d)

print(solution(a,b,c,d))
def solution(points): 
    x_sort = sorted(points)
    y_sort = sorted(points, key =lambda x:x[1])

    x_len = x_sort[-1][0] - x_sort[0][0]
    y_len = y_sort[-1][1] - y_sort[0][1]

    return x_len * y_len
 
import sys
input = sys.stdin.readline

points = [tuple(map(int, input().strip().split())) for _ in range(int(input()))]
print(solution(points))
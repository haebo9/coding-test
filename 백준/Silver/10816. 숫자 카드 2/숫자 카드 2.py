import sys
input = sys.stdin.readline 

n = int(input())
n_array = list(map(int, input().strip().split()))
n_array = sorted(n_array)

m = int(input())
m_array = list(map(int, input().strip().split()))

from bisect import bisect_left, bisect_right
def solution(n_array, target): 
    """
    정렬된 배열에서 같은 값이 있다면
    (타깃의 초과하는 값의 인덱스 - 타깃 이상인 값의 인덱스)는 1 이상이다. 
    """
    # target이 위치한 첫번째 위치 (타깃보다 크거나 같은 값이 시작되는 곳) 
    end = bisect_left(n_array, target)
    # target이 위치한 마지막 위치 (타킷보다 큰 값이 시작되는 곳 = 초과) 
    start = bisect_right(n_array, target)

    return start-end

for target in m_array: 
    print(solution(n_array, target), end = ' ')
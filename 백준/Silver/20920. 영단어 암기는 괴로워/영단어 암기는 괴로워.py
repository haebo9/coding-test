import sys
input = sys.stdin.readline

from collections import Counter
n, m = map(int, input().strip().split())

# 글자 빈도를 담은 튜플 
counter = Counter([input().strip() for _ in range(n)]).most_common()

# 길이를 추가한 리스트 
lst = [(i[0], i[1], len(i[0])) for i in counter if len(i[0]) >= m ]

# 기준에 따라 정렬
sorted_lst = sorted(lst, key= lambda x: (-x[1], -x[2], x[0]))

# 단어만 출력
print(*map(lambda x: x[0], sorted_lst), sep='\n')
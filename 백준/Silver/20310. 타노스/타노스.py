from collections import Counter
import sys
input = sys.stdin.readline
c = Counter(input().strip())
print('0'*(c['0']//2) + '1'*(c['1']//2))
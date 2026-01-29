import sys
input = sys.stdin.readline

words = {input().strip() for _ in range(int(input()))}

sorted_words = sorted(words, key = lambda x: (len(x), x) )

print(*sorted_words, sep= '\n')
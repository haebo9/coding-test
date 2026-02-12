def isPalindrome(s, l, r, cnt): 
    if l >= r: 
        return 1, cnt
    elif s[l] != s[r]: 
        return 0, cnt
    else: 
        cnt += 1
        return isPalindrome(s, l+1, r-1, cnt)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    l = 0 
    r = len(s)-1
    print(*isPalindrome(s, l, r, cnt=1))
from collections import Counter
import sys
# user = input().upper()
user = sys.stdin.readline().strip().upper()

cnt = Counter(user)
answer = cnt.most_common(2)

if len(answer) > 1:
    if (answer[0][1] == answer[1][1]): 
        print('?')
    else: 
        print(answer[0][0])
else: 
    print(answer[0][0])    
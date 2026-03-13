from collections import Counter 
import sys
input = sys.stdin.readline 

# 두 Counter 객체를 입력으로 받음 
def diff(target, word): 
    if target == word: 
        return True
    
    else: 
        diff1 = target - word
        diff2 = word - target 

        if ( diff1 and sum(diff1.values())==1 ) and not diff2: 
            return True # 빼기 
        
        elif ( diff2 and sum(diff2.values())==1 ) and not diff1: 
            return True # 더하기
        
        elif (diff2 and diff1) and (sum(diff2.values())==1) and (sum(diff1.values())==1): 
            return True # 바꾸기 

        else: 
            return False

n = int(input())
target = Counter(input().strip())
result = []

for _ in range(n-1): 
    word = Counter(input().strip()) 
    result.append(diff(target, word))

print(sum(result))
import sys
a, b, v = map(int, sys.stdin.readline().strip().split())

# 첫째날 일단 a 올라간 것으로 치고 시작 
day =  1 + ( (v-a) / (a-b) ) 

# 마지막날 a 올랐더니 끝났다면? 그냥 올림 처리 해야함
day = (int(day)+ 1 if day> int(day) else int(day))

print(day)
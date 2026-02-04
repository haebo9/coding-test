# -를 +-로 바꾸고 +로 구분하여 split 
# 리스트를 앞에부터 읽어가며 음수 뒤의 양수는 다음 음수가 나올때까지 전부 음수로 변경
# 총 합을 구함 

user = list(map(int, input().strip().replace('-', '+-').split('+')))
sum = 0
minus = 1 # 음수 값을 만나면 -1로 바뀜 

for i in user: 
    if i >= 0: 
        sum += (i * minus)
    else: 
        sum += i
        minus = -1
    
print(sum)
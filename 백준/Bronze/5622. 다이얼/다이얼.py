# 숫자 다이얼 시간을 반환하는 딕셔너리
times = {i:1+i for i in range(1,9+1)}
times[0] = times[9]+1
# print(times)

# 알바벳을 숫자 다이얼로 변환하는 딕셔너리 
alp_to_dit = {
    'A':2, 'B':2,'C':2,
    'D':3, 'E':3, 'F':3, 
    'G':4, 'H':4, 'I':4, 
    'J':5, 'K':5, 'L':5, 
    'M':6, 'N':6, 'O':6, 
    'P':7, 'Q':7, 'R':7, 'S':7, 
    'T':8, 'U':8, 'V':8, 
    'W':9, 'X':9, 'Y':9, 'Z':9, 
}

def make_call(call:str):
    answer = 0
    for i in call: 
        temp = times[alp_to_dit[i]]
        answer += temp
    return answer

call = input()
print(make_call(call))
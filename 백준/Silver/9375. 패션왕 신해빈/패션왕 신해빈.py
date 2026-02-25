# 의상의 종류별 의상 개수를 담은 딕셔너리가 필요 
# 딕셔너리의 키값만큼을 최대 개수로 하는 중복없는 선택 개수 x 선택 했을 때 내부의 요소의 개수(value) 

def cloth_count(cnt): 
    cloth = {}
    for _ in range(cnt): 
        name, kind = input().strip().split()
        if kind not in cloth: 
            cloth[kind] = 0
        cloth[kind] += 1

    result = 1
    for v in cloth.values(): 
        # 특정 옷 유형에 대한 경우 = 하나 골라서 입기(v: 옷 개수) + 아무것도 안입기
        result *= v+1

    return result -1 # 아무것도 입지 않는 경우 빼주기 

import sys
input = sys.stdin.readline 

for _ in range(int(input())): 
    print(cloth_count(int(input())))
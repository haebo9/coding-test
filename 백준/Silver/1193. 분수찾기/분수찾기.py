# 1 2 3 4 5 6 .....K ; K번째 1개씩 늘어남 
# 자기 층 개수만큼 늘어남 
# 총 수의 값은? = K+1 * (K) / 2

# 우 좌 우 좌 우 좌 ... 

# 값은 5/1 -> 분보 + 1, 분자 -1 

def value_move(value, move, odd):
    if odd:  
        value[0] -= move-1
        value[1] += move-1
    else: 
        value[0] += move-1
        value[1] -= move-1
    return value

import sys
input = sys.stdin.readline
x = int(input())
layer = 1

while True: 
    total_layer = ((layer+1) * (layer)) // 2
    # print(total_layer)

    if x <= total_layer: # 해당 층에 있다는 뜻
        total_layer_before = ((layer) * (layer-1)) // 2
        if x ==1: move = 1
        elif x ==2: move = 1
        elif x ==3: move = 2
        else: move = x - total_layer_before # x가 양 끝에서 몇번째 인지? 
        # print('move:', move)

        if layer % 2 ==0: # 짝 / 좌측
            value = [1,layer]
            # print('value:',value)
            value = value_move(value, move, odd=False)
        else: # 홀 / 우측
            value = [layer,1]
            # print('value:',value)
            value = value_move(value, move, odd=True)
        break

    else: 
        layer += 1


print(f'{value[0]}/{value[1]}')
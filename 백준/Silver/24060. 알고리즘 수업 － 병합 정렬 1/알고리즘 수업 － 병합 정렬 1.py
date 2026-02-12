def merge_sort(a_lst, p, r):  
    """
    전반부와 후반부를 나누어 정렬한 뒤 병합하는 방식의 정렬 방법 
    """
    if p < r: 
        q = (p+r) // 2 
        merge_sort(a_lst, p, q) 
        merge_sort(a_lst, q+1, r) 
        merge(a_lst, p, q, r)

def merge(a_lst, p, q, r):
    global count, result 
    i, j = p, q+1
    temp = []

    # 두 구간 비교하여 temp에 담기 
    while i <= q and j <= r: 
        if a_lst[i] <= a_lst[j]: 
            temp.append(a_lst[i])
            i += 1
        else: 
            temp.append(a_lst[j])
            j += 1
    
    # 남은 요소들 처리
    while i <= q: 
        temp.append(a_lst[i])
        i += 1
    while j <= r: 
        temp.append(a_lst[j])
        j += 1
    
    t = 0
    for idx in range(p, r+1): 
        a_lst[idx] = temp[t]
        count += 1
        if count == k: 
            result = a_lst[idx]
        t += 1

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
a_lst = list(map(int, input().strip().split()))

count = 0
result = -1

merge_sort(a_lst, 0, n-1)
print(result)
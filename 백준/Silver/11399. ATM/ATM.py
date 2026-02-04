n = int(input())
p_lst = list(map(int, input().strip().split()))

def check_p(p_lst):
    i_sum = 0
    total_sum = 0 

    for i in sorted(p_lst):
        i_sum += i
        total_sum += i_sum 

    return total_sum

print(check_p(p_lst))
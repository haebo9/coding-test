import sys

score_total = 0 # 학점 * 과목평점 의 합
num_total = 0 # 학점의 합

def alp_to_score(alp):
    map_dic = {'A+':4.5, 'A0':4.0, 
               'B+':3.5, 'B0':3.0, 
               'C+':2.5, 'C0':2.0, 
               'D+':1.5, 'D0':1.0, 
               'F':0.0}
    return map_dic[alp]

for _ in range(20):
    user = sys.stdin.readline().strip().split()
    # user = input().split()
    if user[2] == 'P': 
        pass
    else: 
        score_total += (float(user[1])*alp_to_score(user[2]))
        num_total += float(user[1])

print(score_total/num_total)
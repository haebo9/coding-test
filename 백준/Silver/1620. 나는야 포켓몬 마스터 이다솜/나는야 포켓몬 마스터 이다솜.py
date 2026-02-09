import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

# 번호-포켓몬이름 매칭 딕셔너리
num_poket = {str(i) : input().strip() for i in range(1, n+1)}
poket_num = {v:k for k, v in num_poket.items()}

# 확인하려는 값(이름 혹은 번호)
target = [input().strip() for _ in range(m)] 
result = [num_poket[i] if i.isdigit() else poket_num[i] for i in target]

print(*result, sep='\n')
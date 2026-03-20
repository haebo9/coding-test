N, game = input().split()
names = set([input().strip() for _ in range(int(N))])

games = {'Y':2, 'F':3, 'O':4}
print(len(names)//(games[game]-1))
string = input()

alphabet = {chr(i):-1 for i in range(97, 122+1)}

for i,s in enumerate(string): 
    if alphabet[s] == -1:
        alphabet[s] = i
print(' '.join(map(str, alphabet.values())))

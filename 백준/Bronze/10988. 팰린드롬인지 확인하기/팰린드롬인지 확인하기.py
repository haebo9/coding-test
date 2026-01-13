def pelin_check(string):
    for i in range(len(string)//2):
        if string[i] != string[-i-1]:
            return False
    else: 
        return True

string=input()
print(int(pelin_check(string)))
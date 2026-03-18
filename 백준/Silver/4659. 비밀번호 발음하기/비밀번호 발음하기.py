def chechq(string): 
    vowel = set(['a','e', 'i','o','u'])
    str_set = set(string)

    # 조건 1
    if not vowel & str_set: 
        return False

    # 조건 2
    str_b1 = ''
    str_b2 = ''

    b1 = ''

    for i in string: 
        # 조건 1
        if str_b1 == '': 
            str_b1 = (i in vowel)
        elif str_b2 == '': 
            str_b2 = str_b1
            str_b1 = (i in vowel)
        else: 
            if (i in vowel) and str_b1 and str_b2: 
                return False
            elif not (i in vowel) and not str_b1 and not str_b2: 
                return False
            else: 
                str_b2 = str_b1
                str_b1 = (i in vowel)

        # 조건 2
        if b1 == '': 
            b1 = i
        else: 
            if i == b1: 
                if i == 'e' or i == 'o': 
                    continue
                else: 
                    return False
            else: 
                b1 = i

    return True

import sys
input = sys.stdin.readline 

while True: 
    string = input().strip()
    if string == 'end': 
        break 

    result = chechq(string)
    print(f'<{string}> is {'' if result else 'not '}acceptable.')
def kantoer(string): 
    """
    문자열을 삼 등분 한 뒤 앞 뒤 부분만 반환
    """
    if len(string) == 1: 
        return '-'
    slen = len(string)//3
    return kantoer(string[0:slen]) + ' '*slen + kantoer(string[-slen:])

import sys
for line in sys.stdin: 
    n = int(line.strip())

    string = '-'*(3**n)
    print(kantoer(string))    
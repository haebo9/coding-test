match_dict = {'(':')',
              '[':']'}

def check_vps(data:str)->bool:
    stack = []
    for i in data:
        if i in ['(', '[']:
            stack.append(i)
        elif i in [')', ']']:
            if stack:
                if match_dict[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
            else: 
                return False
        elif i == '.':
            break

    if not stack: # 비어있으면
        return True
    else: # 안비어있으면
        return False
    print(stack)

user = ''
while True: 
    user = input()
    if user == '.': 
        break
    else:
        print('yes' if check_vps(user) else 'no')
lst = []
for _ in range(5):
    temp = list(input())
    temp.extend([' ']*(15-len(temp)))
    lst.append(temp)

# print(lst)

lst_zip = list(zip(*lst))
result = ''.join([''.join(i) for i in lst_zip]).replace(' ', '')
print(result)
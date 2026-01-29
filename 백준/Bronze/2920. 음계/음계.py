def check(nums):
    if nums == '1 2 3 4 5 6 7 8':
        return 'ascending'
    elif nums == '8 7 6 5 4 3 2 1':
        return 'descending'
    else: 
        return 'mixed'

nums = input()
print(check(nums))
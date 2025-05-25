s = input('문자열 입력: ')

s = list(s)
s.sort() # 숫자 -> 알파벳순

nums = 0
alpha = ''
for k in s:
    if k.isdigit():
        nums += int(k)
    else:
        alpha += k

print(alpha + str(nums))

def dongbin(s):
    result = []
    nums = 0

    for char in s:
        if char.isalpha():
            result.append(char)
        elif char.isdigit():
            nums += int(char)
    
    result.sort()

    if nums != 0: # 숫자가 하나라도 존재하는 경우 뒤에 삽입**
        result.append(str(nums))

    return ''.join(result)
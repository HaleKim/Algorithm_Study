n = int(input())
for i in range(n):
    guar = input()
    left=0
    right=0
    for g in guar:
        if g == '(':
            left+=1
        else:
            right+=1
        if left - right < 0:
            print('NO')
            break
    if left - right == 0:
        print('YES')
    elif left - right > 0:
        print('NO')
n = int(input())
stac = []
ans = []
for _ in range(n):
    k = input()
    if k.split()[0] == 'push':
        stac.append(k.split()[1])
    elif k == 'front':
        ans.append(stac[0] if stac else '-1')
    elif k == 'back':
        ans.append(stac[-1] if stac else '-1')
    elif k == 'pop':
        ans.append(stac.pop(0) if stac else '-1')
    elif k == 'size':
        ans.append(str(len(stac)))
    elif k == 'empty':
        ans.append('0' if stac else '1')
    else:
        print('잘못입력하셨습니다.')

print('\n'.join(ans))
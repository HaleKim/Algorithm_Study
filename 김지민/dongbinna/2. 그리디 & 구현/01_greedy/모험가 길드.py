n = int(input('모험가 수: '))
k = list(map(int, input('모험가의 공포도: ').split()))

k.sort()
group, cnt = 0, 0
for fear in k:
    cnt += 1
    if fear <= cnt:
        group += 1
        cnt = 0

print(group)

def count_groups(n, k): # 예외 생기는 코드
    ''' 반례
    n = 6
    k = [1, 1, 1, 1, 5, 5]
    '''
    k.sort(reverse = True)
    check = k

    i , group= 0, 0
    while True:
        if k[i] <= len(check):
            group += 1
            i = i + k[i]
            if i >= n:
                break

            check = k[i:]

    return group
    

def solution(n, arr1, arr2):
    a = []
    arr = arr1 + arr2
    answer = []
    for i in arr:
        bi = bin(i)[2:]
        while len(bi) < n:
            bi = '0' + bi
        a.append(bi)
    b = a[:len(a)//2]
    c = a[len(a)//2:]
    ans = [[b[i], c[i]] for i in range(n)]
    for i in ans:
        a1, a2 = i
        jo = ''
        for j in range(n):
            if a1[j] == '1' or a2[j] == '1':
                jo += '#'
            else:
                jo += ' '
        answer.append(jo)
    return answer
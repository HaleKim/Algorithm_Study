def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = ''.join([i for i in alpha if i not in skip])

    for i in s:
        answer+=alpha[(alpha.index(i)+index)%len(alpha)]
    return answer
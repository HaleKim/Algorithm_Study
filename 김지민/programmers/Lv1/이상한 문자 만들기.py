def solution(s):
    answer, check = '', ''
    cnt = 0
    
    for ch in s:
        if ch == ' ':
            cnt += 1
            for i, ch in enumerate(check):
                if i % 2 == 0:
                    answer += ch.upper()
                else:
                    answer += ch.lower()
            answer  += (' '*(cnt))
            check = ''
            cnt = 0
        else:
            check += ch
            
    if check:
        for i, ch in enumerate(check):
            if i % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()

    return answer
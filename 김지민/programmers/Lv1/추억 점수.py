def solution(name, yearning, photo): # 처음 풀이
    answer = []
    
    alpha = {n:y for n, y in zip(name, yearning)}

    for p in photo:
        cnt = 0
        for n in p:
            if n in alpha.keys():
                cnt += alpha[n]
            else:
                cnt += 0
        answer.append(cnt)
    
    return answer

def solution2(name, yearning, photo): # 두 번째 풀이
    answer = []
    
    alpha = {n:y for n, y in zip(name, yearning)}

    for p in photo:
        cnt = 0
        for n in p:
            cnt += alpha.get(n, 0)
        answer.append(cnt)
    
    return answer

def solution3(name, yearning, photo): # 세 번째 풀이
    alpha = {n:y for n, y in zip(name, yearning)}

    answer = [sum(alpha.get(n, 0) for n in p ) for p in photo]
    
    return answer
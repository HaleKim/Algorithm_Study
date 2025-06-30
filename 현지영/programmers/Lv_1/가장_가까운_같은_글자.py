def solution(s):
    answer, s2 = [], ''
    for i,w in enumerate(list(s)):
        if w in s2 :
            answer.append(i-(s2.rfind(w)))
        else :
            answer.append(-1)
        s2 = s2+w
    return answer
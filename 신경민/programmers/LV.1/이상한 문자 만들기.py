def solution(s):
    answer = ''
    s = s.lower()
    a = s.split()
    test = ''
    n=0
    for k in a:
        for i,j in enumerate(k):   
            if i%2 == 0:
                test+=j.upper()
            else:
                test+=j
    for i in s:
        if i.isalpha():
            answer+=test[n]
            n+=1
        else:
            answer+=' '
    return answer
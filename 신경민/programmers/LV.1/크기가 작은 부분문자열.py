def solution(t, p):
    answer = 0
    n=0
    num_lis=[]
    while(True):
        num_lis.append(t[n:n+len(p)])
        if n+len(p) == len(t):
            break
        n+=1
    for i in num_lis:
        if i <= p:
            answer+=1
    return answer
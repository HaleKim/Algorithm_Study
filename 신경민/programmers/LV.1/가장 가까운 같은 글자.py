def solution(s):
    first = []
    find={}
    answer=[]
    for i,j in enumerate(s):
        if j in first:
            answer.append(i-find[j])
            find[j] = i
        else:
            answer.append(-1)
            find[j] = i
            first.append(j)
    return answer
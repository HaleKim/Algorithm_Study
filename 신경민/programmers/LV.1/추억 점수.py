def solution(name, yearning, photo):
    answer=[]
    n_set = {name[i]:yearning[i] for i in range(len(name))}
    for i in photo:
        plu = 0
        answer.append(sum([n_set[j] for j in i if j in name]))
    return answer
def solution(name, yearning, photo):
    answer = []
    for photos in photo :
        score = 0
        for p in photos :
            if p in name:
                i = name.index(p)
                score += yearning[i]
        answer.append(score)
    return answer
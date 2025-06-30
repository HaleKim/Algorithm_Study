def solution(k, score):
    answer = []
    result = []
    for s in score :
        answer.append(s)
        answer= sorted(answer)
        if len(answer) > k:
            answer = answer[1:]    
        result.append(answer[0])
    return result
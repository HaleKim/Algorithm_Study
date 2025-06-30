def solution(cards1, cards2, goal):
    for g in goal :
        if cards1 != [] and g in cards1[0] :
            result = 'Yes'
            cards1.remove(g)
        elif cards2 != [] and g in cards2[0] :
            result = 'Yes'
            cards2.remove(g)
        else :
            result = 'No'
            break
    return result
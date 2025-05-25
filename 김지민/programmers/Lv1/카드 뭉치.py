def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    g_c1, g_c2 = [], []
    for g in goal:
        if g in cards1:
            g_c1.append(g)
        else:
            g_c2.append(g)

    for g, c in zip(g_c1, cards1):
        if g != c:
            answer = 'No'
            break
    for g, c in zip(g_c2, cards2):
        if g != c:
            answer = 'No'
            break
        
    return answer
def solution(cards1, cards2, goal):
    
    for i in range(len(goal)) :
        if cards1 and goal[i] == cards1[0] : # cards1의 첫번째 문자열 확인인
            cards1.pop(0) # 순서대로 문자열을 꺼내야 하니 pop(0) 수행
            
        elif cards2 and goal[i] == cards2[0]:
            cards2.pop(0)
            
        else :
            return 'No'
    
    return 'Yes'

    

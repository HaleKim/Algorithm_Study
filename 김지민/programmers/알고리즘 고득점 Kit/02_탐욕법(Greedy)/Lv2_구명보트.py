def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    for p in people:
        total = p
        if len(people) != 1:
            back = people.pop()
            total += back
            if total > limit:
                people.append(back)
        answer += 1
        
    return answer
def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * n

    for i in range(n):
        if i+1 in reserve:
            clothes[i] += 1
        if i+1 in lost:
            clothes[i] -= 1
    
    for i in range(n):
        if clothes[i] == 0:
            if i > 0 and clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] += 1
            elif i < n-1 and clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] += 1

    for c in clothes:
        if c >= 1:
            answer += 1

    return answer


'''인덱스 오류 발생
    if clothes[0] == 2 and clothes[1] == 0:
        clothes[0] -= 1
        clothes[1] += 1
            
    if clothes[-1] == 2 and clothes[-2] == 0:
        clothes[-1] -= 1
        clothes[-2] += 1
    
    for i, c in enumerate(clothes):
        if c == 0:
            if clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] += 1
            elif clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] += 1'''
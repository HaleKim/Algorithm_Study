def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        A = numbers[i]
        for j in range(i+1,len(numbers)):
            B = numbers[j]
            C = A + B
            if C in answer :
                continue
            else :
                answer.append(C)
            
            
            
    return sorted(answer)
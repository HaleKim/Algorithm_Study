def solution(n, lost, reserve):
    lost_ = list(set(lost) - set(reserve))
    reserve_ = list(set(reserve) - set(lost))
    answer = n - len(lost_)
        
    for std in lost_ :
        for rstd in reserve_ :
            if std + 1 == rstd or std - 1 == rstd :
                reserve_.remove(rstd)
                answer += 1
                break
                
    return answer
def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    cnt = n - len(lost)
    i = 0
    
    while(True):
        if i >= len(reserve):
            break
        elif reserve[i] in lost:
            cnt += 1
            lost.remove(reserve[i])
            reserve.remove(reserve[i])
        else:
            i+=1
    
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            cnt += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            cnt += 1
    
    return cnt
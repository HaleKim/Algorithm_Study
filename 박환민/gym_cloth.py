def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    not_rob = n - len(lost_set)
    
    for i in lost_set:
        if i-1 in list(reserve_set):
            reserve_set.remove(i-1)
            not_rob += 1
        elif i+1 in list(reserve_set):
            reserve_set.remove(i+1)
            not_rob += 1
                
    return not_rob
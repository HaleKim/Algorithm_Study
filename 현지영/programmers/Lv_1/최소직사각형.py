def solution(sizes):
    a1, a2 = 0, 0
    for size in sizes :
        max_ = max(size)
        min_ = min(size)
        if max_ > a1 :
            a1 = max_
        if min_ > a2 :
            a2 = min_
    answer = a1 * a2
    return answer
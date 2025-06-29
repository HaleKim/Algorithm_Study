def solution(nums):
    answer = []
    m = len(nums)/2 
    for n in nums :
        if n not in answer :
            answer.append(n)
    # if m <= len(answer) :
    #     return m
    # elif m > len(answer) :
    #     return len(answer)
    return min(m, len(answer))

def solution2(nums):
    answer = []
    m = len(nums)/2 
    type_ = set(nums)
    return min(m, type_)
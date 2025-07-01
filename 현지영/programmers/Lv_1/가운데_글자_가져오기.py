def solution(s):
    s_ = list(s)
    x = len(s_) // 2
    if len(s_) % 2 == 0 :
        ans = s_[x-1]+s_[x]
    else :
        ans = s_[x]
    
    answer = ans
    return answer
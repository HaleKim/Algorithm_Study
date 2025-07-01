def solution(s):
    if len(list(s))==4 or len(list(s))==6 :
        return s.isdigit()
    else :
        return False
    
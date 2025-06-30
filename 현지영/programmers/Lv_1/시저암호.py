def solution(s, n):
    Alpha1 = 'abcdefghijklmnopqrstuvwxyz'
    Alpha2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    answer = ''
    for word in s :
        if word in list(Alpha1) :
            ans = Alpha1.split(word)
            ans_ = str(ans[1])+str(ans[0])
            answer+=ans_[n-1]

        elif word in list(Alpha2) :
            ans = Alpha2.split(word)
            ans_ = str(ans[1])+str(ans[0])
            answer+=ans_[n-1]
         
        else :
            answer+=' '
            
    return answer
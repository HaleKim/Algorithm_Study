def solution(s):
    answer = ''
    for s1 in s.split(' ') :
        ans = ''
        for i, ss in enumerate(s1) :
            if i % 2 == 0 :
                ans += ss.upper()
            else :
                ans += ss.lower()
        answer += (ans+' ')
    return answer[:-1]
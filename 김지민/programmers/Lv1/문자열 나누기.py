def solution(s): # 처음 풀이
    answer = 0

    ch1 = s[0]
    cnt1, cnt2 = 0, 0

    for i in range(len(s)):
        if ch1 == s[i]:
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 == cnt2:
            answer += 1
            cnt1, cnt2 = 0, 0
            if i+1 < len(s):
                ch1 = s[i+1]
                
    if cnt1 != 0 or cnt2 != 0:
        answer += 1

    return answer


def solution2(s): # 나중 풀이
    i, answer = 0, 0
    
    while i < len(s):
        n1, n2 = 1, 0
        st = s[i]
        i += 1
        
        while i < len(s):
            if s[i] == st:
                n1 += 1
            else:
                n2 += 1
            i += 1
            
            if n1 == n2:
                break
        
        answer += 1
                
    return answer

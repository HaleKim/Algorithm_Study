def solution(answers):
    ans = []
    ss1,ss2,ss3 = 0,0,0
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)) :
        if answers[i] == s1[i%5] :
            ss1 += 1
        if answers[i] == s2[i%8] :
            ss2 += 1
        if answers[i] == s3[i%10] :
            ss3 += 1

    if ss1 == max(ss1,ss2,ss3) :
        ans.append(1)
    if ss2 == max(ss1,ss2,ss3) :
        ans.append(2)
    if ss3 == max(ss1,ss2,ss3) :
        ans.append(3)
    
    return ans
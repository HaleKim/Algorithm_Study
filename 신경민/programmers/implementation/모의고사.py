def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    who=[]
    for i in [supo1, supo2, supo3]:
        n=0
        i *= (len(answers)//len(i))+1
        for j in range(len(answers)):
            if answers[j] == i[j]:
                n+=1
        who.append(n)
    for i,j in enumerate(who):
        if j == max(who):
            answer+=[i+1]
    return answer
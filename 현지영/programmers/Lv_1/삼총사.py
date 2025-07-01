def solution(num):
    count = 0
    for i in range(len(num)-2) :
        for j in range(i+1, len(num)-1) :
            for k in range(j+1, len(num)) :
                if num[i]+num[j]+num[k] == 0 :
                    count+=1
    return count
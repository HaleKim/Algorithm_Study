def solution(n):
    cnt=0
    li = [0]*n
    for i in range(1,n+1) :   #  1부터 n까지
        for j in range(i,n+1,i) :
            li[j-1]+=1
    for A in li :
        if A == 2:
            cnt+=1
    return cnt

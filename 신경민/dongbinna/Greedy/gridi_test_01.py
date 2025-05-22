def wone(n,k):
    cnt = 0
    while(True):
        if n % k == 0:
            cnt+=(n//k)
            break
        else:
            n-=1
            cnt+=1
    return cnt
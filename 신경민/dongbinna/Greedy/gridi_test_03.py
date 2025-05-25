def guild(n,s):
    s = sorted([int(i) for i in s.split()])[::-1]
    cnt = 0
    while(True):
        if not s or len(s) < s[0]:
            break
        elif len(s) == s[0]:
            s=[]
            cnt+=1
        else:
            for _ in range(s[0]):
                s.pop(0)
            cnt+=1
    return cnt

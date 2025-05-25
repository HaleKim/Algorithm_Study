def bignum(s):
    s = list(s)
    ans = int(s[0])
    for i in s[1:]:
        if ans == 0 or i == '1' or i == '0':
            ans+=int(i)
        else:
            ans*=int(i)
    return ans

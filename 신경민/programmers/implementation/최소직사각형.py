def solution(sizes):
    big = []
    sbig = []
    for i in sizes:
        a,b = i
        big+=i
        if a < b:
            sbig.append(a)
        elif a==b:
            sbig.append(a)
        else:
            sbig.append(b)
    return max(big)*max(sbig)
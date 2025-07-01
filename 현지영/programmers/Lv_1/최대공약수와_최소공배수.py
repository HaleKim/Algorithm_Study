def solution(n, m):
    X = 0
    for i in range(1,min(n,m)+1) :
        if n%i==0 and m%i==0 :
            X = i
    return [X, n*m/X]
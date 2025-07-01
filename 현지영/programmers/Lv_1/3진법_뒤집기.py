def solution(n):
    a3 = []
    while n != 0 :
        a3 = [n%3] + a3
        n = n // 3
    ans = 0
    for i,a in enumerate(a3) :
        ans += a*(3**(i))
    return ans
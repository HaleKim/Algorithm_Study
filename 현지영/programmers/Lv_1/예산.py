def solution(d, budget):
    money = 0

    d = sorted(d)
    for i, t in enumerate(d) :
        money += t
        if money > budget :
            ans = i
            break
        ans = i+1
    return ans
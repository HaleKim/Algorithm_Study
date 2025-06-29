def solution(food):
    ans = []
    for i, f in enumerate(food[1:]) :
        if f%2 == 1:
            f = int((f-1)/2)
        else:
            f = int(f/2)
        if f == 0 :
            continue
        else:
            for _ in range(f) :
                ans.append(i+1)

    ans2 = []
    for i in range(len(ans)) :
        ans2.append(ans[-(i+1)])

    answer = ''
    
    for a in ans+[0]+ans2:
        answer+=str(a)
    return answer
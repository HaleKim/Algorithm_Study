def solution(babbling):
    can = ['aya','ye','woo','ma']
    can2, can3, can4 = [], [], []
                    
    for i in range(len(can)) :
        for j in range(len(can)) :
            if j == i :
                continue
            w = can[i] + can[j]
            can2.append(w)
            for k in range(len(can)) :
                if k == i or k == j:
                    continue
                w = can[i] + can[j] + can[k]
                can3.append(w)
                for l in range(len(can)) :
                    if l == i or l ==j or l == k:
                        continue
                    w = can[i] + can[j] + can[k] +can[l]
                    can4.append(w)

    cnt = 0
    for b in babbling :
        if len(b) <= 3:  # 한 개 조합 (2 or 3)
            if b in can :
                cnt+=1
        elif len(b) <= 6 : #두 개 조합 (4 or 5 or 6)
            if b in can2 :
                cnt+=1
        elif len(b) <= 8 : #세 개 조합 (7 or 8)
            if b in can3 :
                cnt+=1
        elif len(b) == 10 : #네 개 조합 (10)
            if b in can4 :
                cnt+=1
    return cnt
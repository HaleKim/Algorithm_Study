while True:
    a = input()
    if a == 'end': break

    mo = cntm = cntj = 0
    prev = ''
    accep = True

    for i in a:
        if i in 'aeiou':   
            cntm +=1
            mo += 1
            cntj=0
        else:
            cntj+=1
            cntm=0
        if cntm == 3 or cntj == 3 or (i == prev and i not in 'eo'):
            accep = False
            break
        prev = i

    print(f'<{a}> is {"acceptable" if accep and mo else "not acceptable"}.')

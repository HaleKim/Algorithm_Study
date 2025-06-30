def solution(s):
    answer = ''
    eng = ['one','two','three','four','five','six','seven','eight','nine','zero']
    num = ['1','2','3','4','5','6','7','8','9','0']
    dic = dict(zip(eng, num))
    print(dic)
    s = list(s)
    #print(s)
    print(''.join(s[:3]))
    while s != [] :
        if ''.join(s[:3]) in eng :
            answer += dic[''.join(s[:3])]
            s = s[3:]
        elif ''.join(s[:4]) in eng :
            answer += dic[''.join(s[:4])]
            s = s[4:]
        elif ''.join(s[:5]) in eng :
            answer += dic[''.join(s[:5])]
            s = s[5:]
        else :
            answer += s[0]
            s = s[1:]    
    return int(answer)
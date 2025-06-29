money = int(input())
juga = list(map(int, input().split()))

def jun(money, juga) :
    jusic = 0
    for j in juga :
        if money == 0 :
    #        print(jusic)
            continue
        jusic += (money // j)
        money = (money % j)
    #    print(jusic)
    return money + juga[-1]*jusic

def seong(money, juga) :
    jusic = 0 
    j_1 = juga[0]
    plus, minus = 0, 0
    for j in juga[1:] :
        if j_1 < j : # 상승
            plus += 1  # 상승 스택
            minus = 0  # 하락 초기화
        elif j_1 > j :  # 하락
            plus = 0   # 상승 초기화
            minus += 1 # 하락 스택
        j_1 = j
        if plus == 3 : # 상승 3스택
            money += j * jusic
            jusic = 0
            plus = 0
        if minus == 3 : # 하락 3스택
            jusic += (money // j)
            money = (money % j)
            minus = 0
    return money + juga[-1]*jusic

j_money = jun(money, juga)
s_money = seong(money, juga)
if j_money > s_money :
    print('BNP')
elif j_money < s_money :
    print('TIMING')
else :
    print('SAMESAME')

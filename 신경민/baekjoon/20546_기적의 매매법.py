def dnp(money, chart):
    jusik=0
    for juga in chart:
        if money >= juga:
            jusik += (money // juga)
            money %= juga
    return chart[-1]*jusik + money

def timing(money, chart):
    jusik = 0
    cnt_up = 0
    cnt_donw = 0
    yes_juga = chart[0]
    for now_juga in chart[1:]:
        if now_juga < yes_juga:
            cnt_donw = 0
            cnt_up += 1
            if cnt_up >= 3:
                jusik += (money // now_juga)
                money %= now_juga
                cnt_up=0
        elif now_juga > yes_juga:
            cnt_up = 0
            cnt_donw += 1
            if cnt_donw >= 3:
                money += jusik * now_juga
                jusik = 0
                cnt_donw=0
        yes_juga = now_juga
    return chart[-1] * jusik + money

n = int(input())
chart = list(map(int, input().split()))
if dnp(n, chart) > timing(n, chart):
    print('BNP')
elif dnp(n, chart) < timing(n, chart):
    print('TIMING')
else:
    print('SAMESAME')
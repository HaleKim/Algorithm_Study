cash_junhyun = cash_sungmin = int(input())
stock = list(map(int, input().split()))
stock_n_junhyun = 0
stock_n_sungmin = 0
buy_n_junhyun = 0
buy_n_sungmin = 0


for i in stock :
    if cash_junhyun >= i  :
        buy_n_junhyun = cash_junhyun // i
        stock_n_junhyun += buy_n_junhyun
        cash_junhyun = cash_junhyun - buy_n_junhyun * i


# 조건별 전량 매수, 전량 매도
for i in range(len(stock)-3) :
    # 전량 매도는 언제든 가능
    if stock[i] < stock[i+1] < stock[i+2] :
        cash_sungmin += stock_n_sungmin * stock[i+3]
        stock_n_sungmin = 0

    # 전량 매수는 돈이 있을때만 가능
    if stock[i] > stock[i+1] > stock[i+2]:
        if cash_sungmin >= stock[i+3]:
            buy_n_sungmin = cash_sungmin // stock[i+3]
            stock_n_sungmin += buy_n_sungmin
            cash_sungmin -= buy_n_sungmin * stock[i+3]


final_price = stock[-1]
junhyun_total = cash_junhyun + stock_n_junhyun * final_price
sungmin_total = cash_sungmin + stock_n_sungmin * final_price

if junhyun_total > sungmin_total:
    print("BNP")
elif sungmin_total > junhyun_total:
    print("TIMING")
else:
    print("SAMESAME")
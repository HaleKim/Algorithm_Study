def solution(price, money, count):
    p = 0
    while count > 0 :
        p += price
        money -= p
        count -= 1
    if money >= 0 :
        return 0
    else :
        return money * -1
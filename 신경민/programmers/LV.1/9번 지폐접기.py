def solution(wallet, bill):
    answer = 0
    while max(bill) > max(wallet) or min(wallet) < min(bill):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer+=1
    return answer
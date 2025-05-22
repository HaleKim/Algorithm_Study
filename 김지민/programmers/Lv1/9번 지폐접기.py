def solution(wallet, bill):
    answer = 0
    st_max, st_min = max(wallet), min(wallet)

    while max(bill) > st_max or min(bill) > st_min:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //=2
        answer += 1

    return answer

def solution2(wallet, bill): # 좋은 풀이
    wallet, bill = sorted(wallet), sorted(bill)
    cnt = 0

    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[-1] //= 2
        bill = sorted(bill)
        cnt += 1
    return cnt
    
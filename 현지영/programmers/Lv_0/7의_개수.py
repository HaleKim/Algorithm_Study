def solution(array):
    count = 0
    for ar in array :
        print(ar, type(ar))
        while ar != 0 :
            if ar % 10 == 7 :
                count += 1
            ar = ar // 10
    return count
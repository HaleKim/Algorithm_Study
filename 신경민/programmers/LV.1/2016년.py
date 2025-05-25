def solution(a, b):
    answer = ''
    d=0
    cal = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    for i in range(a-1):
        if i+1 in [1,3,5,7,8,10,12]:
            d += 31
        elif i+1 == 2:
            d += 29
        elif i+1 in [4,6,9,11]:
            d += 30
    answer = cal[(d+b)%len(cal)-1]
    return answer
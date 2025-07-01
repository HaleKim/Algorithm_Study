def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30]
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = sum(month[:a])+b
    print(days)
    return week[days%7-1]

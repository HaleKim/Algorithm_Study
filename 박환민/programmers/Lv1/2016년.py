import datetime

def solution(a, b):
    
    d_2016 = f'2016-{a}-{b}'
    d_day = datetime.datetime.strptime(d_2016, "%Y-%m-%d").date()
    
    date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    return date[d_day.weekday()]
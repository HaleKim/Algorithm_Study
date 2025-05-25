def solution(a, b):
    cal = {
        0:'THU', 1:'FRI', 2:'SAT', 
        3:'SUN', 4:'MON', 5:'TUE', 6:'WED'
    }
    
    day = 0
    month = 1 
    while month < a:
        if month in [1,3,5,7,8,10,12]:
            day += 31
        elif month == 2:
            day += 29
        elif month in [4,6,9,11]:
            day += 30
        month += 1
            
    day += b
    
    return cal[day % 7]
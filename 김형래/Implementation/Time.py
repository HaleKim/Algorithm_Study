# from datetime import time
# from datetime import timedelta

# time(0,0,0)

n = int(input())

# for hour in range(n) :
#     for minute in range(60) :
#         for second in range(60) :
#             time[2] += 1
print(sum(1 for hour in range(n+1) for minute in range(60) for second in range(60) if '3' in str(second) or '3' in str(minute) or '3' in str(hour)))

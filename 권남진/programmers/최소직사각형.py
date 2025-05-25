# 프로그래머스 >
# 최소 직사각형


def solution(sizes):
#     max__len = [60,70,60,80]
#     min__len = [50,30,30,40]
#     sortmax_len = [80,70,60,60]
#     sortmin_len = [50,40,30,30]

#     max__len = [10,12,15,14,15]
#     min__len = [7,3,8,7,5]
#     sortmax_len = [15,15,14,12,10]
#     sortmin_len = [8,7,7,5,3]
    
#     max__len = [14,19,16,18,11]
#     min__len = [4,6,6,7,7]
#     sortmax_len = [15,15,14,12,10]
#     sortmin_len = [8,7,7,5,3]
    max_length,min_length = [],[]
    
    for i in sizes:
        
        
        max_length.append(max(i))
        # max_length.sort(reverse = True)
        
        min_length.append(min(i))
        # min_length.sort(reverse = True)
        
    return max(max_length) * max(min_length)

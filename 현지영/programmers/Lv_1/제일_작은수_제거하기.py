def solution(arr):
    s_num, idx = arr[0], 0
    for i in range(len(arr)) :
        if s_num > arr[i] :
            s_num = arr[i]
            idx = i
    del arr[idx]
    if len(arr) == 0:
        answer = [-1]
    else :
        answer = arr
        
    return answer
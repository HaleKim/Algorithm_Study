def solution(arr):
    answer = []
    x = arr[0]
    answer.append(x)
    for a in arr :
        if a != x :
            answer.append(a)
        x = a
    return answer
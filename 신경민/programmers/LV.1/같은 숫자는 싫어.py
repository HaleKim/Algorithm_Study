def solution(arr):
    a=arr[0]
    answer=[arr[0]]
    for i in arr:
        if i != a:
            answer.append(i)
            a=i
        else:
            continue
    return answer
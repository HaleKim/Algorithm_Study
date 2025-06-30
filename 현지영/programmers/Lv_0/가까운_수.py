def solution(array, n):
    minus = [abs(n-i) for i in array]
    min_x = min(minus)
    ans = array[minus.index(min_x)]
    for i, x in enumerate(minus) :
        if x == min_x :
            if array[i] < ans :
                ans = array[i]         
    return ans
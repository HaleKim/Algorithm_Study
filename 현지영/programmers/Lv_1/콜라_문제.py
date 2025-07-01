def solution(a, b, n):
    answer = 0
    total = n
    while total >= a :
        n = total//a
        answer += n*b
        total = n*b+int(total%a)
        
    return answer
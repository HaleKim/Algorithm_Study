def solution(num, k):
    answer = ''

    while k != 0 and num:
        check = num[:k+1]
        max_digit = max(check)
        answer += max_digit
        idx = check.index(max_digit)
        k -= idx
        num = num[idx+1:]
           
    answer+=num
    
    return answer

print(solution('1924',2))
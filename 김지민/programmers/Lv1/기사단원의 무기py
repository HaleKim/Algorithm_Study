def solution(number, limit, p_limit): # 내 코드
    answer = 1
    
    for soldier in range(2, number+1):
        i, power = 1, 0
        
        while i <= soldier ** 0.5:
            if soldier % i == 0:
                power += 2
            i += 1
            if i == soldier ** 0.5: 
                power -= 1
            
        if power > limit:
            power = p_limit
            
        answer += power
    
    return answer

def solution1(number, limit, p_limit): # solution() 수정 후 코드
    answer = 1
    
    for soldier in range(2, number+1):
        power = 0
        for i in range(1, int(soldier**0.5)+1):
            if soldier % i == 0:
                power += 2
                if i == (soldier//i):
                    power -= 1
            
        if power > limit:
            power = p_limit
        answer += power
    
    return answer

def solution2(number, limit, limit_power): # 시간 초과 오류 (처음 풀이)
    answer = 0
    
    for n in range(1, number+1):
        power = 0
        for i in range(1, n+1):
            if n % i == 0:
                power += 1
        if power > limit:
            power = limit_power
        answer += power
    
    return answer
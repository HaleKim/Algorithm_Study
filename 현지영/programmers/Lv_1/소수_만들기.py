from itertools import combinations

def is_prime(n):
    if n ==0 or n==1 :
        return False
    else :
        for i in range(2, (n//2)+1):
            if n % i == 0:
                return False 
        return True 

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))       
    for arr in cmb:
        if is_prime(sum(arr)):       
            answer += 1                     
    
    return answer
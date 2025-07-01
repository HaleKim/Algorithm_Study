def solution(numlist, n):
    answer = sorted(numlist, key = lambda x:(abs(x-n),-x))    
    return answer
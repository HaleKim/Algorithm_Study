def solution(nums):
    from itertools import combinations as cb
    
    s = []
    for i in list(cb(nums, 3)): # 콤비네이션 함수를 통해 3개의 모든 숫자 조합 생성 
        s.append(sum(i)) # 3개의 숫자의 합을 s에 추가

    cnt = 0
    for i in s :
        for j in range(2,i) : 
            if i % j == 0 :
                break # 나눠지는 수가 1과 자기자신 뿐이라면 break (횟수 카운트 X)
        else :
            cnt+= 1 # 소수라면 cnt +1
            
    return cnt

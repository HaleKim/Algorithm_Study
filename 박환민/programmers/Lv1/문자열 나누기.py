def solution(s):
    
    x = s[0] # 처음 문자를 x로 초기화
    cnt = 1
    diff_cnt = 0
    same_cnt = 1 
    
    for i in range(1, len(s)-1): # s[i+1]로 새로 초기화하므로 len(s)-1로 해주어야함
        if s[i] != x : # 처음 나온 문자와 다른 문자라면
            diff_cnt += 1 # 다른 문자가 나온 횟수 +1
        else : # 처음 나온 문자와 같은 문자라면
            same_cnt += 1 # 같은 문자가 나온 횟수 +1
            
        if diff_cnt == same_cnt : # 횟수가 서로 같아졌다면
            x  = s[i+1] # 처음 문자를 다시 초기화
            cnt += 1 # 문자열을 나눈 횟수 +1
        
    return cnt


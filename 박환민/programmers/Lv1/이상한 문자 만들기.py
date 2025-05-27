def solution(s):
    
    answer = ''
    s = s.lower()
    index = 0
    
    for i in range(len(s)): # 문자열을 순회
        if s[i] == ' ': # 문자가 공백인 경우
            answer += s[i] # 공백도 그대로 추가
            index = 0 # 마지막 공백을 기준으로 다음 문자의 인덱스를 0으로 초기화
        
        else : 
            if index % 2 == 0:
                answer += s[i].upper()
                index += 1
            else :
                answer += s[i]
                index += 1
        
        
    return answer

        
        
        
        
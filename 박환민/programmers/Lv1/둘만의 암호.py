def solution(s, skip, index):
    
    answer = []
         
    for i in s :
        cnt = 0 # 알파벳 변경 횟수를 문자마다 초기화
        next_alpha = i
        while cnt < index : # cnt가 index가 되기 전까지 반복문 수행
            if next_alpha == 'z' : # 현재 알파벳이 z일 경우, 예외 처리
                next_alpha = 'a'
            else :
                next_alpha = chr(ord(next_alpha) + 1) # 알파벳을 하나씩 뒤의 알파벳으로 변경
                
            if next_alpha not in set(skip) : # 다음 알파벳이 skip할 알파벳이 아니라면
                cnt += 1 # 알파벳 변경 횟수 +1
                
        answer.append(next_alpha)
    
    return ''.join(answer)
                
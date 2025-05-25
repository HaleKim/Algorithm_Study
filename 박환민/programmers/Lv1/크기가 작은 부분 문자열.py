def solution(t, p):
    answer = 0
    
    substr = []
    for i in range(len(t)): # t 문자열을 순회
        if len(t[i:i+len(p)]) == len(p): # p 문자열의 길이만큼 부분문자열 인덱싱
            substr.append(t[i:i+len(p)]) # substr에 부분 문자열을 추가
    
    for i in list(map(int,substr)) : # 부분 문자열을 int형으로 변환
        if i <= int(p) : # p보다 부분 문자열의 크기가 작다면 
            print(i)
            answer += 1 # 개수 +1
            
    return answer
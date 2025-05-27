def solution(s):
    
    check = {}
    
    result = []
    
    for i in range(len(s)): # 주어진 문자열 순회
        if s[i] not in check : # 처음 나온 문자라면
            result.append(-1) # -1 반환
        else : # 처음 나온 문자가 아니라면
            result.append(i - check[s[i]]) # (현재 인덱스 - 이전위치의 인덱스) = 거리를 추가
            
        check[s[i]] = i # 문자와 해당 위치를 check 딕셔너리에 추가

    return result
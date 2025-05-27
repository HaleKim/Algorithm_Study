def solution(s):
    
    sub = ['zero','one','two','three','four','five','six','seven','eight','nine']
    sub_map = ['0','1','2','3','4','5','6','7','8','9']
    
    for i in range(len(sub)):
        if sub[i] in s: # 주어진 문자열을 순회하며 영단어 찾기
            s = s.replace(sub[i],sub_map[i]) # 영단어를 숫자 문자열로 변환

    return int(s)
def solution(s):
    answer, word = [], ""
    words = "zero one two three four five six seven eight nine".split()
    wtn = {word : str(num) for num, word in zip(range(10), words)} # 매핑
    
    for c in s : # s 순회
        if c.isdigit() : # 숫자를 만난 경우
            if word : # 저장된 영단어 존재
                for w in words : # 매핑
                    if word.find(w) >= 0 :
                        word = word.replace(w,wtn[w])
                answer.append(word)
                word = ""
            answer.append(c)
        else : # 문자를 만난 경우
            word += c
    
    if word : # s가 영단어로 끝나는 경우
        for w in words : # 매핑
            if word.find(w) >= 0 :
                word = word.replace(w,wtn[w])
        answer.append(word)
    
    return int("".join(answer))

# 분명 긴 컨테이너를 수정하는 것은 지양해야 하지만, 문제 조건을 잘 보고 골라서 하자..
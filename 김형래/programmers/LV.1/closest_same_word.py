def solution(s):
    answer, sub = [], ""
    for c in s : # 순회
        idx = sub.rfind(c) # rfind로 가장가까운놈 찾기
        if idx >= 0 :
            answer.append(len(sub) - idx) # 거리 구하기
        else :
            answer.append(-1) # 없으믄 -1
        sub += c
    return answer
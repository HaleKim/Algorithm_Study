# 1. 각 위치에서 가장 가까운 다음 변경위치로 이동
# ABBBAAAB 반례 발견
# 2. 변경할 문자열이 더 적은 위치로 이동 ?

def getYdist(char) :
    return ord(char) - 65 if char <= 'N' else 26 - (ord(char) - 65)

def solution(name):
    answer = 0
    idx, Pdist, Ndist, Cidx, length = 0,0,0,0,len(name) 
    # 인덱스, +이동거리, -이동거리, 커서위치, 이름길이
    nameList = list(name)
    # 문자열은 인덱싱하여 수정이 불가능하므로 list로 변환

    while True :
        if nameList.count('A') == length : # 변환 완료되면 while 탈출
            break
        Cidx = idx
        if nameList[idx] == 'A' : # 현재위치가 A면 이동해야한다
            idx += 1 # +방향 이동
            if idx >= length :
                idx %= length
            while nameList[idx] == 'A' :
                idx += 1
                if idx >= length :
                    idx %= length
            Pdist = abs(Cidx-idx)
            idx = Cidx-1 # 원위치 후 -방향 이동
            if idx < -length :
                idx %= length
            while nameList[idx] == 'A' :
                idx -= 1
                if idx < -length :
                    idx %= length
            Ndist = abs(Cidx-idx)
        if Pdist > Ndist : # -방향 이동이 더 가까울때
            idx = (Cidx - Ndist) % length
            answer += Ndist
        else : # +방향 이동이 더 가까울때
            idx = (Cidx + Pdist) % length
            answer += Pdist
        answer += getYdist(nameList[idx])
        nameList[idx] = 'A'
        
        Pdist, Ndist = 0,0 # 변수 초기화
        # print("변환 후 : %s %d" % (nameList, answer))
        
    return answer

# def solution(name):
#     print(-8 % 6)
# 음수의 나머지연산 공부 필요
def solution(name, yearning, photo):
    answer = []
    
    for i in photo : 
        cnt = 0 # 배열이 바뀔때마다 그리움 점수 초기화
        for j in range(len(i)) : # photo에 있는 이름을 탐색
            if i[j] in name : # photo에 그리움 점수가 있는 이름이 존재한다면
                cnt += yearning[name.index(i[j])] # name 에서 해당 이름의 인덱스를 찾아 yearning의 인덱스로 지정
        answer.append(cnt)
        
    return answer
def solution(name):
    length = len(name)
    xmove, ymove = length-1, 0
    for i in range(length) :
        ymove += ord(name[i]) - 65 if name[i] <= 'N' else 91 - ord(name[i])
        # 65 : ord('A') 91 : ord('Z') + 1 (시작지점이 A이므로 + 1)
        nextidx = i + 1
        # 다음 index
        while nextidx < length and name[nextidx] == 'A' :
            nextidx += 1
        # 연속된 A는 넘기는 과정
        xmove = min(xmove, i*2 + length-nextidx, (length-nextidx)*2 + i)
        # 최적의 거리를 고르는(최소 거리를 고르는) 과정 : 1,2,3 비교
        # 1. 처음부터 오른쪽 끝까지 한 번에 이동 : length-1
        # 2. 처음부터 현재 위치 i까지 왔다가 다시 처음 위치로 돌아간 후 nextidx까지 이동            : (i*2) + (length-nextidx)
        # 3. 처음부터 nextidx까지 왼쪽(-방향) 으로 갔다가 다시 돌아온 후 nextidx까지 이동 : (length-nextidx)*2 + i
        # 이 과정을 name을 순회하면서 수행 (이해를 돕기 위한 괄호를 넣었음!)
    return xmove + ymove
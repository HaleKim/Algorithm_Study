# from collections import deque

# answerList = []
# cases = int(input())

# for _ in range(cases) :
#     flag, idx, answer, queue = False, 0, 0, deque()
#     n, m = map(int, input().split())
#     for inum in map(int, input().split()) :
#         queue.append((idx, inum))
#         idx += 1
#     if n == 1 :
#         answerList.append(1)
#         continue
#     while queue :
#         flag = True
#         i, now = queue.popleft()
#         for j, num in queue :
#             if num > now : # 넘김
#                 queue.append((i,now))
#                 flag = False
#                 break
#         if i == m : # 정답
#             answer += 1
#             answerList.append(answer)
#             break
#         elif flag : # 출력
#             answer += 1

# for ans in answerList :
#     print(ans)

# ---------------------------------------------------------------------
# 루프 구성 변경 : 정답 처리를 flag == true 내부에 이동
# 이전 코드는 재삽입되는 경우에도 i == m 이면 answer를 증가시킴.
# ---------------------------------------------------------------------

from collections import deque

answerList = []
cases = int(input().strip())

for _ in range(cases):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    queue = deque()
    
    # (초기 인덱스, 중요도) 저장
    for idx, priority in enumerate(docs):
        queue.append((idx, priority))
    
    printed = 0  # 인쇄된 문서 수
    while queue:
        current = queue.popleft()
        printable = True
        
        # 현재 문서보다 중요도 높은 문서 있는지 확인
        for doc in queue:
            if doc[1] > current[1]:
                queue.append(current)
                printable = False
                break
                
        if printable:
            printed += 1  # 인쇄 카운트 증가
            if current[0] == m:  # 찾는 문서인 경우
                answerList.append(printed)
                break

for ans in answerList:
    print(ans)
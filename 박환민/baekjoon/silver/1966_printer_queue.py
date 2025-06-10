import sys
from collections import deque

# input = sys.stdin.readline
answer = []

T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N, M = map(int, input().split())
    importance = deque(map(int, input().split()))

    # 문서 큐: 0,1,2,...,N-1 로 식별
    document = deque(range(N))

    # 내가 관심 있는 문서는 M번 위치의 문서
    target = document[M]

    cnt_print = 0
    while importance:
        v = importance.popleft()
        doc = document.popleft()

        # 뒤에 더 중요한 문서가 하나라도 있으면 맨 뒤로
        if any(v < imp for imp in importance):
            importance.append(v)
            document.append(doc)
        else:
            # 인쇄
            cnt_print += 1
            if doc == target:
                answer.append(cnt_print)
                break

print('\n'.join(map(str,answer)))
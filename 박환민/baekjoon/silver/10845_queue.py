# 큐는 선입선출
from collections import deque

N = int(input())

queue = deque()

answer = []

for i in range(N):
    cmd_list = input().split()
    cmd = cmd_list[0]

    if cmd == 'push':
        queue.append(cmd_list[1])

    elif cmd == 'pop':
        if queue :
            answer.append(queue[0])
            queue.popleft()
        else :
            answer.append(-1)

    elif cmd =='size':
        answer.append(len(queue))

    elif cmd == 'empty':
        if queue :
            answer.append(0)
        else :
            answer.append(1)

    elif cmd == 'front':
        if queue :
            answer.append(queue[0])
        else :
            answer.append(-1)
    elif cmd == 'back' :
        if queue :
            answer.append(queue[-1])
        else :
            answer.append(-1)

print('\n'.join(map(str,answer)))
# 스택은 선입후출
N = int(input())

stack = []

answer = []

for i in range(N):
    cmd_list = input().split()
    cmd = cmd_list[0]

    if cmd == 'push':
        stack.append(cmd_list[1])

    elif cmd == 'pop':
        if stack :
            answer.append(stack[-1])
            stack.pop()
        else :
            answer.append(-1)

    elif cmd =='size':
        answer.append(len(stack))

    elif cmd == 'empty':
        if stack :
            answer.append(0)
        else :
            answer.append(1)

    elif cmd == 'top':
        if stack :
            answer.append(stack[-1])
        else :
            answer.append(-1)

print('\n'.join(map(str,answer)))
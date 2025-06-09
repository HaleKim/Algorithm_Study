import sys
N=int(sys.stdin.readline())
stack=[]
for _ in range(N):
    command=sys.stdin.readline().split() #split
    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0]=='size':
        print(len(stack))
    elif command[0]=='empty':
        print(1 if not (stack) else 0)
    elif command[0]=='top':
        print(stack[-1] if stack else -1)
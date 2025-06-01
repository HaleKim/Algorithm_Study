n = int(input())
command_list = []
for _ in range(n) :
  command_list.append(input().split())

stack = []

for command in command_list :
  match command[0] :
    case "push" :
      stack.append(command[1])

    case "pop" :
      try :
        p = stack.pop()
      except IndexError :
        p = -1
      finally :
        print(p)
      
    case "size" :
      print(len(stack))

    case "empty" :
      if stack :
        print(0)
      else :
        print(1)

    case "top" :
      if stack :
        print(stack[-1])
      else :
        print(-1)
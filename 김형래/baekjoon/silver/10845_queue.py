from collections import deque

n = int(input())
command_list = []
for _ in range(n) :
  command_list.append(input().split())

queue = deque()

for command in command_list :
  match command[0] :
    case "push" :
      queue.append(command[1])

    case "pop" :
      try :
        p = queue.popleft()
      except IndexError :
        p = -1
      finally :
        print(p)
      
    case "size" :
      print(len(queue))

    case "empty" :
      if queue :
        print(0)
      else :
        print(1)

    case "front" :
      if queue :
        print(queue[0])
      else :
        print(-1)

    case "back" :
      if queue :
        print(queue[-1])
      else :
        print(-1)
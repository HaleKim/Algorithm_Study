n = int(input())

coords = []
for _ in range(n) :
  coords.append(list(map(int, input().split())))

for coord in sorted(coords, key=lambda x:(x[0],x[1])) :
  print("%d %d" % (coord[0],coord[1]))
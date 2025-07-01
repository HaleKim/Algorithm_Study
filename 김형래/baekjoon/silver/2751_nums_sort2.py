import sys

n = int(sys.stdin.readline())

decs = []
for _ in range(n) :
  decs.append(int(sys.stdin.readline()))

for num in sorted(decs) :
  print(num)
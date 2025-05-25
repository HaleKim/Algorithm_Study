s = input()
s = sorted(s)

answer = ""
num = 0
for c in s :
  if c.isdigit() :
    num += int(c)
  else :
    answer += c

print(answer + str(num))
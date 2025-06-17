# 중첩 for문 탈출법 ?

import sys

pw_list = []
vowels = ['a','e','i','o','u']

while True :
  pw = sys.stdin.readline().strip()
  if pw == "end" : break
  else : pw_list.append(pw)

for pw in pw_list :
  available = False
  for vowel in vowels : # 1번 조건
    if vowel in pw : available = True
  if not available : 
    print("<%s> is not acceptable." % pw)
    continue

  if available :
    vcnt, ccnt = 0, 0
    for c in pw : # 2번 조건
      if c in vowels : 
        ccnt = 0
        vcnt += 1
      else :
        vcnt = 0
        ccnt += 1
      if ccnt == 3 or vcnt == 3 :
        print("<%s> is not acceptable." % pw)
        available = False
        break

  if available :
    for i in range(1, len(pw)) : # 3번 조건
      if pw[i-1] == pw[i] :
        if pw[i] == 'e' or pw[i] == 'o' : continue
        else :
          print("<%s> is not acceptable." % pw)
          available = False
          break
  
  if available : # 모든 조건 만족
    print("<%s> is acceptable." % pw)
# print(ord('a')) : 97

nowi = input()

rowdict = {chr(c) : n for c, n in zip(range(97, 106), range(8))}
row, col = rowdict[nowi[0]], int(nowi[1])
answer = 0
# coordinate = [[i for i in range(8)] for _ in range(8)]

if row+2 <= 7 :
  if col+2 <= 7 :
    answer += 1
  if col-2 >= 0 :
    answer += 1

if row-2 >= 0 :
  if col+2 <= 7 :
    answer += 1
  if col-2 >= 0 :
    answer += 1

if col+2 <= 7 :
  if row+2 <= 7 :
    answer += 1
  if row-2 >= 0 :
    answer += 1

if col-2 >= 0 :
  if row+2 <= 7 :
    answer += 1
  if row-2 >= 0 :
    answer += 1

print(answer)

# 똥
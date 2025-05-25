from functools import reduce

s = input()
s = s.replace('0', '')
print(reduce(lambda x,y : x*y, [int(c) for c in s]) + s.count('1'))
# 두 번 순회 => 성능 down
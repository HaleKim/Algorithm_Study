# 딕셔너리가 리스트 보다 시간복잡도가 더 빠름 => 리스트는 O(n) 순회하지만 딕셔너리는 키값으로 바로 찾음
n, m = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(n):
    a = input()
    name_to_num[a] = i+1
    num_to_name[i+1] = a

for _ in range(m):
    a = input()
    if a.isdigit():
        print(num_to_name[int(a)])
    else :
        print(name_to_num[a])
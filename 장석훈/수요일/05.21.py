# PCCE 기출 1번/출력 
string_msg = 'Spring is beginning'

int_val = 3

string_val = '3'


print(string_msg)
print(int_val + 10)
print(string_val + "10")

# PCCE 기출 1번/ 문자 출력
message = "Let's go!"

print("3\n 2\n 1")
print(message)

# lv.1 최소직사각형
bigest_list=[]
second_list=[]
def solution(sizes):
    # #가로 길이 리스트
    # for i in range(0,len(sizes)):
    #     w_list.append(sizes[i][0])
    # #세로 길이 리스트
    # for i in range(0,len(sizes)):
    #     h_list.append(sizes[i][1])
    for i in range(len(sizes)):
        a,b=sizes[i]
        if a<b:
            bigest_list.append(b)
            second_list.append(a)
        else:
            bigest_list.append(a)
            second_list.append(b)
    return max(bigest_list)*max(second_list)


















'''모양과 크기를 모두 수납, 작아서 편한
가로80, 세로 50의 크기는 4000
import pandas as pd
import numpy as np
w_list=[]
h_list=[]
a,b=sizes
#가로 길이 리스트
for i in range(0,len(sizes)):
    w_list.append(sizes[i][0])
#세로 길이 리스트
for i in range(0,len(sizes)):
    h_list.append(sizes[i][1])
w=max(w_list)
h=max(h_list)

if w>h: 
answer=w*h
answer

##
w_list=[]
h_list=[]
sizes=[[60,50],[30,70],[60,30],[80,40]]
#가로 길이 리스트
for i in range(0,len(sizes)):
    w_list.append(sizes[i][0])
#세로 길이 리스트
for i in range(0,len(sizes)):
    w_list.append(sizes[i][1])

w=max(w_list)
w_list.remove(w)
h=max(h_list) '''
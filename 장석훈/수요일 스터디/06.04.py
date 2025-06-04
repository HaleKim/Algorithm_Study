#1966 프린터큐

# 입력   N, M 
#       [N개의 중요도]

from collections import deque
import sys
# tc = sys.stdin.readline().rstrip()

N, M= map(int, input().split())
if not M<N:
    print('error')
priority=list(map(int,input().split()))
priority.sort()
que=deque(priority)
cnt=0
while True:
    if que[0]==priority[-1]:
        que.popleft()
        priority.pop()
        cnt+=1
        if M==0:
            break
    else:
        que.append(que.popleft())
        if M==0:
            M=len(que)-1
        else: 
            M-=1
print(cnt)


# 프로그래머스 시저코드
def solution(s, n):
    
alphabet=['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ALPHABET=[i.upper() for in alphabet]
answer=''
for i in s:
    if i in alpha:
        string=alpha.index(i)+n
        if string>25:
            string%=26
        answer+=alpha[string]
    elif i in ALPHABET:
        string=ALPHABET.index(i)+n
        if string>25:
            string%=26
        answer+=alpha[string]
    else: #공백일때
        answer+=' '
return answer
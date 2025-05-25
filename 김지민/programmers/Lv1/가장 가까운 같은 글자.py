# 정답률 74%
def solution(string): #처음 풀이
    answer = []
    check = ''
    
    for i, s in enumerate(string):
        if s not in check:
            answer.append(-1)
            check += s
        else:
            answer.append(i - check.index(s))
            check = check.replace(s, '*')
            check += s
    
    return answer

def solution2(string): # 더 좋은 풀이
    answer = []
    last = {}
    
    for i, s in enumerate(string):
        if s not in last:
            answer.append(-1)
        else:
            answer.append(i - last[s])
        last[s] = i
            
    
    return answer
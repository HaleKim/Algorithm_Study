# 정답률 79%
def solution(arr): # 내 풀이
    answer = []
    
    i = 0
    while i < len(arr):
        ch = arr[i]
        answer.append(ch)
        
        while i+1 < len(arr) and arr[i+1] == ch :
            i += 1
            
        i += 1

    return answer

def solution2(arr): # 간결한 풀이
    answer = []
    
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer
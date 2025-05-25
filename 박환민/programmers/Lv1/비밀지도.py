def solution(n, arr1, arr2):
    
    bin_arr1 = []
    bin_arr2 = []
    answer = []
    
    for i,j in zip(arr1,arr2) :
        # 배열의 요소마다 10진수를 2진수로 변환
        bin_arr1.append(format(i, f'0{n}b'))  
        bin_arr2.append(format(j, f'0{n}b'))
        
        
    # 2진수로 변환 후
    for i, j in zip(bin_arr1, bin_arr2):
        answer.append(''.join('#' if (a == '1') | (b == '1') else ' ' for a, b in zip(i,j))) # 하나라도 1 이 존재하면 #, 그렇지 않으면 ' '을 반환
        
    return answer

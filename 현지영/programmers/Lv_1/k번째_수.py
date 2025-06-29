def solution(array, commands):
    answer = []
    for c in commands :
        i, j, k = c[0], c[1], c[2]
        n_array = array[i-1:j]
        s_array = sorted(n_array)
        print(s_array)
        ans = s_array[k-1]
        answer.append(ans)    
    
    return answer
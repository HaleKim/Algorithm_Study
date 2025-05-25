def solution(sizes):
    
    w = []
    h = []
    
    for i in sizes :
        w.append(i[0]) # 가로길이 리스트
        h.append(i[1]) # 세로길이 리스트
             
    
    for i in range(len(sizes)) :
        if sizes[i][0] > sizes[i][1] : 
            print('check')
        else :
            w[i] = sizes[i][1] # 가로, 세로중 길이가 긴 경우를 가로 리스트에 넣어줌(명함 돌리기)
            h[i] = sizes[i][0]
            
    print(max(w), max(h))
        
    return max(w) * max(h)
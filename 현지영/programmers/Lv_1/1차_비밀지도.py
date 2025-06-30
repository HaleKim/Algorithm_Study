def solution(n, arr1, arr2):
    answer = []
    max_l = max(max(len(bin(a)) for a in arr1),
                max(len(bin(a)) for a in arr2)) - 2
    for a1, a2 in zip(arr1,arr2) :
        total = str(int(bin(a1)[2:]) + int(bin(a2)[2:]))
        while len(total) != max_l :
            total = '0'+total
        ans = ''
        for t in total :
            if t == '0' :
                ans += ' '
            else :
                ans += '#'
        answer.append(ans)
    return answer
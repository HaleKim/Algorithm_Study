def solution(s, skip, index): # 내 코드
    answer = ''
    check = []

    for ch in s:
        ch = ord(ch)
        while len(check) != index:
            ch = ch+1
            if ch > ord('z'):
                ch = ch - 26
            if chr(ch) in skip:
                continue
            check.append(chr(ch))
        answer += check[-1]
        check = []

    return answer

def solution2(s, skip, index): # 좋은 코드
    skip = set(skip)
    answer = ''
    
    for ch in s:
        cnt = 0
        curr = ord(ch)
        
        while cnt < index:
            curr += 1
            if curr > ord('z'):
                curr -= 26
            if chr(curr) in skip:
                continue
            cnt += 1
        answer += chr(curr)

    return answer
def solution(name):
    spell_move = 0
    for i in range(len(name)):
        if ord(name[i]) - ord('A') < 13:
            spell_move += ord(name[i]) - ord('A')
        else:
            spell_move += ord('Z') - ord(name[i]) +1
    
    cursor_move = len(name)-1
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        print(i, next, [cursor_move, 2*i + len(name)-next, 2*(len(name)-next) + i])
        cursor_move = min([cursor_move, 2*i + len(name)-next, 2*(len(name)-next) + i])
        

    return spell_move + cursor_move

print(solution('TAATAAAAAT'))
# print(solution('JEROSN')) 
# print(solution('BBBABBB'))
# print(solution('JAN'))
# https://html-jc.tistory.com/650

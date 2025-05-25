# 정답률 72%
def solution(string):
    answer, alpha = '', ''
    a_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3',
              'four':'4', 'five':'5', 'six':'6', 'seven':'7',
              'eight':'8', 'nine':'9'}
    
    for s in string:
        if s.isdigit():
            answer += s
        else:
            alpha += s
            if alpha in a_dict:
                answer += a_dict[alpha]
                alpha = ''

    return int(answer)
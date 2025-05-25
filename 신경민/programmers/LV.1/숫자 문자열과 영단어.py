def solution(s):
    alpha_lis = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    alpha_dict={}
    answer = []
    n = 0
    for i, j in enumerate(alpha_lis):
        alpha_dict[j] = str(i)
    while(True):
        if n == len(s):
            break
        elif s[n].isdigit():
            answer.append(s[n])
            n+=1
        elif s[n:n+3] in alpha_lis:
            answer.append(alpha_dict[s[n:n+3]])
            n +=3
        elif s[n:n+4] in alpha_lis:
            answer.append(alpha_dict[s[n:n+4]])
            n +=4
        elif s[n:n+5] in alpha_lis:
            answer.append(alpha_dict[s[n:n+5]])
            n +=5
        else:
            break
    return int(''.join(answer))

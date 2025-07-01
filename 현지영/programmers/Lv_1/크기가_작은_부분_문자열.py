def solution(t, p):
    count = 0
    for i in range(len(t)-len(p)+1) :
        if p >= t[i:i+len(p)] :
            count += 1
    return count
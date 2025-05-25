def make_binary(n, arr):
    binary = []
    for a in arr:
        a = bin(a)[2:]
        a = a.rjust(n, '0') # '0'*(n-len(a)) + a
        binary.append(a)
    return binary

def solution(n, arr1, arr2):
    answer = []
    
    binary1 = make_binary(n,arr1)
    binary2 = make_binary(n,arr2)

    for b1, b2 in zip(binary1, binary2):
        line = ''
        for i in range(n):
            if b1[i] == '1' or b2[i] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
        
    return answer
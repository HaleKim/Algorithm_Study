def solution(number, k):
    stack = []
    
    for n in number:
        while len(stack)>0 and stack[-1] < n and k != 0:
            stack.pop()
            k -= 1
        stack.append(n)
        
    if k != 0:
        return number[:-k]
    else:
        return ''.join(stack)
print(solution('10', 1)) #1
print(solution('333222111', 3)) #333222
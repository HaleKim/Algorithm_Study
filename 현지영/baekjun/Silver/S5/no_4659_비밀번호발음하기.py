# 비밀번호 발음하기

# 가장 이상적인 해결법은 '발음이 가능한' 패스워드를 만드는 것으로 
# 적당히 외우기 쉬우면서도 안전하게 계정을 지킬 수 있다. 

# 회사 FnordCom은 그런 패스워드 생성기를 만들려고 계획중이다. 
# 당신은 그 회사 품질 관리 부서의 직원으로 생성기를 테스트해보고 
# 생성되는 패스워드의 품질을 평가하여야 한다. 
# 높은 품질을 가진 비밀번호의 조건은 다음과 같다.


# 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

mo = ['a','e','i','o','u']

while True :
    x=y=0
    password = input()
    if password == 'end' :
        break
    cnt = 0
    for m in mo :
        if m in password :
            cnt += 1
    if cnt <1 :
        print(f'<{password}> is not acceptable.')
        continue
    for i in range(len(password)-2) :
        if password[i] in mo and password[i+1] in mo and password[i+2] in mo :
            x = 1
        elif not (password[i] in mo) and not (password[i+1] in mo) and not (password[i+2] in mo) :
            x = 1
    if x == 1 :
        print(f'<{password}> is not acceptable.')
        continue
    for i in range(len(password)-1) :
        if password[i]==password[i+1] :
            if password[i]=='e' or password[i]=='o' :
                continue
            else:
                y = 1
    if y == 1:
        print(f'<{password}> is not acceptable.')
        continue
    print(f'<{password}> is acceptable.')

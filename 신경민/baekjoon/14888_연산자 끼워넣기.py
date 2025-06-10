def dfs(n, sm, add, sub, mul, div):
    global mn, mx

    if sm < int(-1e9) or int(1e9)<sm:
        return

    if n==N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return
    
    if add>0:
        dfs(n+1, sm+lst[n], add-1, sub, mul, div)
    if sub>0:
        dfs(n+1, sm-lst[n], add, sub-1, mul, div)
    if mul>0:
        dfs(n+1, sm*lst[n], add, sub, mul-1, div)
    if div>0:
        dfs(n+1, int(sm/lst[n]), add, sub, mul, div-1)    

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)
dfs(1, lst[0], add, sub, mul, div)
print(mx, mn, sep='\n')
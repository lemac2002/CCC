def shift(a,b):
    ans = 0
    for i in range(b+1):
        ans += a*pow(10,i)
    print(ans)

N = int(input())
M = int(input())
shift(N,M)

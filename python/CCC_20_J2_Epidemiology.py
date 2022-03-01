import math

P = int(input())
N = int(input())
R = int(input())
if R > 1:
    M1 = 1 + (P*(R-1)+1)/N
    days = int(math.log(M1,R))
else:
    days = P//N
print(days)

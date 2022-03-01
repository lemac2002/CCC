def compare(a,b,c):
    Occup = 0
    for i in range(c):
        if(a[i] == 'C' and a[i] == b[i]):
            Occup+=1
    print(Occup)

k = int(input())
day1 = input()
day2 = input()

compare(day1,day2,k)

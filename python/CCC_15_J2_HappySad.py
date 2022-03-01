def mood(a):
    index = 0
    happy = 0
    sad = 0
    while index < len(a):
        if index + 2 < len(a) and a[index] == ':' and a[index+1] == '-' and a[index+2] == ')':
            happy +=1
        elif index + 2 < len(a) and a[index] == ':'and a[index+1] ==  '-' and a[index+2] == '(':
            sad +=1
        index += 1
    if happy > sad:
        print("happy")
    elif happy < sad:
        print("sad")
    elif happy == sad and happy != 0 or sad !=0:
        print("unsure")
    else:
        print("none")

A = input()
mood(A)

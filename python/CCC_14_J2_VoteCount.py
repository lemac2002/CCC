def counter (a,b):
    A = 0
    B = 0
    for i in range(a):
        if b[i] == 'A':
           A += 1
        if b[i] == 'B':
            B += 1
    if A > B:
        print("A")
    elif B > A:
        print("B")
    else:
        print("Tie")
num_votes = int(input())
votes = input()

counter(num_votes,votes)

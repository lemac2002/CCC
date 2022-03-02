numbers = []
for i in range(4):
    numbers.append(int(input()))

if numbers[0] == numbers[1] and numbers[1] == numbers[2] and numbers[2] == numbers[3]:
    print("Constant Depth")
elif numbers[0] < numbers[1] and numbers[1] < numbers[2] and numbers[2] < numbers[3]:
    print("Fish Rising")
elif numbers[0] > numbers[1] and numbers[1] > numbers[2] and numbers[2] > numbers[3]:
    print("Fish Diving")
else:
    print("No Fish")

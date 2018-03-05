import random
rezult = random.randint(1,100)
number = 0

while number != rezult:
    number = int(input("Number:"))
    if number > rezult:
        print("Input less")
    elif number < rezult:
        print("Input more")
    elif number == rezult:
        print("Winnnn")

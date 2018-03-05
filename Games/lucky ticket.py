import random
total1 = 0
total2 = 1
quantity = 0
while total1 != total2:
    ticket = random.randint(100000, 999999)
    digit_1 = ticket // 100000
    digit_2 = ticket // 10000 % 10
    digit_3 = ticket // 1000 % 10
    digit_4 = ticket // 100 % 10
    digit_5 = ticket // 10 % 10
    digit_6 = ticket % 10
    total1 = digit_1 + digit_2 + digit_3
    total2 = digit_4 + digit_5 + digit_6
    if total1 == total2:
        print("Lucky you, ticket number", ticket)
    else:
        print("Unlucky you, ticket number", ticket)
        quantity += 1
print(quantity+1)


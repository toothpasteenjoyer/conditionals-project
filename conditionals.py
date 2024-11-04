import random
number = random.randit(0, 100)
guess = int(input("number: "))
while guess != number:
    if guess > number:
        print("go lower")
        guess = int(input("number: "))
    if guess < number:
        print("go higher")
        guess = int(input("number: "))
else:
    print("yippiee!!!")
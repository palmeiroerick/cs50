from random import randint

n = 0

while n < 1:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass

number = randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess < 1:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

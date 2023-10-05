import random

number = random.randint(1, 10)

player = True

guess = int(input("Guess the number (1~10): "))
while True:
    if guess != number:
        if guess < number:
            guess = int(input("Try going Bigger!: "))
        elif guess > number:
            guess = int(input("Try going Lower!: "))

    else:
        if player is True:
            print(f"\nCongratulations! Player 1 is the Winner!")
            break

        elif player is False:
            print(f"\nCongratulations! Player 2 is the Winner!")
            break

    player = not player

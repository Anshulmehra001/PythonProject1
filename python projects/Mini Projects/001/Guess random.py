import random

def guess(x):
    random_number = random.randint(1, x)
    guess = None
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    print(f"Congrats! You have guessed the number {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        while feedback not in ['h', 'l', 'c']:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer guessed your number, {guess}, correctly!")


computer_guess(100)



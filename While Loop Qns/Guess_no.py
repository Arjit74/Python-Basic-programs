import random
num = random.randint(1, 100)

attempts = 0
guess = None

print("Welcome to the Number Guessing Game!")

while guess != num:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess == num:
        print(f"Congratulations! You've guessed the number {num} correctly in {attempts} attempts.")
    elif guess < num:
        print("Try higher.")
    elif guess>100:
        print("Please enter the number between 1 to 100")
    else:
        print("Try lower.")

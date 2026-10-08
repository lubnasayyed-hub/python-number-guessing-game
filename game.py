import random

def guessing_game():

    print("NUMBER GUESSING GAME")  # game title

    print("1. EASY MODE: (1-10)")
    print("2. DIFFICULTY MODE: (1-100)")

    choice = input("Choose The Mode (1 or 2): ")  # choose the mode

    if choice == "1":  # set the number range
        maximum = 10

    elif choice == "2":
        maximum = 100

    else:
        print("Invalid choice!")
        return

    # Secret number generated using random.randint
    number = random.randint(1, maximum)

    attempts = 0  # set the attempt limit
    max_attempts = 5

    print("You have five attempts!")

    while attempts < max_attempts:  # loop for guessing game

        guess = int(input("Enter the guess: "))
        attempts = attempts + 1

        # Compare player's guess with secret number
        if guess < number:
            print("Too Low!")

        elif guess > number:
            print("Too High!")

        else:
            print("Correct!")
            print("You guessed it in", attempts, "attempts")
            return

    # This runs after all 5 attempts are finished
    print("GAME OVER!")
    print("The number was:", number)


guessing_game()  # function calling
import random

def start_game():
    print("Welcome to the Ultimate Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You found it in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Oops! That's not a valid number. Please enter an integer.")

if __name__ == "__main__":
    start_game()

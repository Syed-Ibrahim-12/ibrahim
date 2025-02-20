import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # The computer picks a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0  # Initialize the number of attempts
    
    while True:
        try:
            # Take user input
            user_guess = int(input("Guess a number between 1 and 100: "))
            
            attempts += 1  # Increment the attempt count
            
            # Check if the user's guess is correct
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        
        except ValueError:
            print("Please enter a valid number.")

# Start the game
number_guessing_game()


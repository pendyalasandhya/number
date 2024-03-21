import random

def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I've picked a random number between 1 and 100. Can you guess it?")
    
    # Generate a random number
    target_number = random.randint(1, 100)
    
    # Set the maximum number of attempts
    max_attempts = 5
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess == target_number:
                print(f"Congratulations! You guessed it right in {attempts} attempts.")
                break
            elif user_guess < target_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            if attempts >= max_attempts:
                print(f"Sorry, you've reached the maximum number of attempts. The correct number was {target_number}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_guessing_game()
    else:
        print("Thanks for playing! Have a great day!")

# Start the game
play_guessing_game()
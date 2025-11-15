import random

secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 2  
print("Welcome to the Number Guessing Game!")
player_name = input("Enter your name: ")
print(f"Hello, {player_name}! I'm thinking of a number between 1 and 20.")
while attempts < max_attempts:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations, {player_name}! You've guessed the number {secret_number} in {attempts} attempts!") 
play_again = input("Would you like to play again? (yes/no): ")
if play_again == 'yes':
    secret_number = random.randint(1, 20)
    attempts = 0
    print("Great! I've thought of a new number between 1 and 20.")
    
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations, {player_name}! You've guessed the number {secret_number} in {attempts} attempts!")
    
else:
    print("Thank you for playing! Goodbye!")    
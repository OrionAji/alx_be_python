secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess (between 1 and 10): "))
    guess_count += 1
    
print(f"Congratulations! You've guessed the number {secret_number} in {guess_count} attempts.") 
    
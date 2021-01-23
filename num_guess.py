# Author: Paul Quaife
# Date: 1/20/2021
# Description: Plays higher or lower guessing game with number entered.

print("Enter the integer for the player to guess. ")
ans = int(input())
guesses_taken = 0
print("Enter your guess.")
guess = int(input())
for i in range(guesses_taken, guesses_taken + 1):
    guesses_taken += 0
    if guess == ans:
        print("You guessed it in", guesses_taken + 1, "try.")
        break
    while True:
        guesses_taken = guesses_taken + 1
        if guess < ans:
            print("Too low - try again:")
            guess = int(input())
        if guess > ans:
            print("Too high - try again:")
            guess = int(input())
        elif guess == ans:
            print("You guessed it in", guesses_taken + 1, "tries.")
            break

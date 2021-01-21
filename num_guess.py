# Author: Paul Quaife
# Date: 1/20/2021
# Description: Plays higher or lower guessing game with number entered.

print("Enter the integer for the player to guess.")
ans = int(input())
print("Enter your guess")
guess = int(input())
if guess < ans:
    print("Too low - try again:")
elif guess > ans:
    print("Too high - try again:")
elif guess == ans:
    print("You guessed it in ", guess, "tries.")

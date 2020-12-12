import random
import colorama

high = 1000
low = 1

print("Please think of a numer between {} and {}".format(low, high))
input("Press ENTER to start")

guess = 1

while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {} Should I guess Higher or Lower? Enter H or L or C if the guess is correct\n~".format(guess)).lower()
    if high_low == "h":
        low = ++guess
        print("Guessing HIGHER... How about {}?".format(guess))
    elif high_low == "l":
        high = --guess
        print("Guessing LOWER... How about {}?".format(guess))
    elif high_low == "c":
        print("Hurrah! The answer is {}!".format())
        break

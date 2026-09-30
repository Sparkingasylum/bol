#number guessing game
#generate random number between
import random
number= random.randint(1,10)

#player guess
guess=input("guess a number between 1 and 10:")
guess=int(guess)
#if player guess wrong
if guess==number:
    print("you won")
#stop the guess if right
elif guess <number :
    print("too low, try again!")
else:
    print("too high, try again!")


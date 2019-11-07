# THIS PROGRAM GUESS THE SECRET NUMBER IN YOUR MIND (A GUESS THE NUMBER GAME)
import random

SecretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

# ASK THE GAMER TO GUESS THE SECRET NUMBER SIX TIMES
for GuessTaken in range(1, 7):
    print('Take your guess')
    guess = int(input())

    if guess < SecretNumber:
        print('Your guess is to low...try again')
    elif guess > SecretNumber:
        print('Your guess is high....try again')
    else:
        break

if guess == SecretNumber:
    print('What a Brilliant guess. You guessed my number in ' + str(GuessTaken) + ' guess')
else:
    print('You got it wrong, I guessed ' + str (SecretNumber))


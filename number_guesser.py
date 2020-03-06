#source: https://inventwithpython.com/chapter4.html

import random

guessesTaken = 0

print('Enter Username to Begin')
user = input()

number = random.randint(1, 1000)
print('Hello ' + user + ', I am thinking of a number between 1 and 1000.')

while guessesTaken < 10:
    print('Guess')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print(user + ' you guessed the correct number in ' + guessesTaken + ' guesses.')

if guess != number:
    number = str(number)
    print('The number I was thinking of was ' + number)

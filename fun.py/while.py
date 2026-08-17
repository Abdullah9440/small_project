import random

number = random.randint(1, 100)
guesses = 5

while guesses > 0:

    if guesses == 1:
        print('You have 1 guess left')
    else:
        print(f'You have {guesses} guesses left')

    guess = int(input('Enter your guess: '))

    if guess == number:
        print('Correct guess')
        break
    elif guess < number:
        print('Guess higher than that')
    else:
        print('Guess lower than that')

    guesses -= 1

if guesses == 0:
    print('You lost!')
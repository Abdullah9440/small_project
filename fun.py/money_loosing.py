import random
money = 100
i = 0
while i<10:
    user_guess = input('guess :- ').lower()
    while user_guess  not in  ['head','tails']:
     print('make the right guess')
     user_guess = input('guess :- ').lower()
     
     
    computer_guess = random.choice(['head','tails'])
    if user_guess == computer_guess:
        print('you won the money &9')
        money += 9
        print(f'your money now {money}')
    else:
        print('you loose money &10')
        money -= 10
    print(f'your money now {money}')
    i += 1
print(f'you money now {money}')
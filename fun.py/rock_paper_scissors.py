import random
user = 0
computer = 0
while user < 3 and computer < 3:
     user_input= input('👊 rock, 🧻 paper or ✂️ scissor: ').lower() 
     if user_input not in ('rock','paper','scissor'):
        print('enter the correct spelling')
        user_input= input('👊 rock, 🧻 paper or ✂️ scissor: ').lower() 
     computer_input = random.choice(['rock','paper ','scissor']).lower()
     print('computer choose : ',computer_input)
     if user_input == computer_input:
       print(f'😊 tie ')
     elif (user_input == 'paper' and computer_input == 'rock') or\
        (user_input == 'rock' and computer_input == 'scissor') or \
        (user_input == 'scissor' and computer_input == 'paper'):
        print(f' 🙅‍♂️ Abdullah wins the roung')
        user += 1
     else:
       print(f' 🖥️ Computer wins this round')
       computer += 1
if user == 3:
    print(f'🙅‍♂️ the winner is Abdullah 3 times')
else:
    print(f'🖥️ the winner is computer 3 times')
   
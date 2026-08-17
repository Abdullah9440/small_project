'''i = 1
while i<= 50:
    print(i)
    i += 1'''
    
'''words = input('enter a string')
i = 0
while i <= len(words):
    print(words[i])
    i += 2'''
    
'''w = float(input('enter weight in kelogram : '))
while w < 0:
    print('invalid input,make it corrent')
    w = float(input('enter weight in kelogram : '))
pound = w * 2.20
print("pound : ", pound)'''

'''password = 1234
i = 5
while i > 0:
    try:
        user_input = int(input('ENTER PASSWORD : '))
    except ValueError:
        print(f'that is not a number,try again you have {i} attempt left')
        i -= 1
        continue
    if password == user_input:
        print('logged in')
        break
    else:
        user_input = int(input(f"try again,you have {i} attempt left"))
        i -= 1
else:
    print('you are kicked out')'''
    
    

'''total = 0
star_marks = 0
count = 0
i = 1

while i <= 5:
    try:
         score = int(input('enter your score'))
    except ValueError:
        print('enter the right score')
        continue
    i = i+1
    total += score
    
    count += 1
    
    if score > 90:
        
        star_marks += 1
average = total / count
print(star_marks)
print(f"and the average is {average}")'''





    
        



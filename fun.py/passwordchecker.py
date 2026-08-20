info = {
    
    'abdullah': '123',
    'anik' : '234',
    'hasan': '345'
}
user = input('enter your name and password')
if user in info:
 password = input('enter your password')
 if password == info[user]:
     print('you are logged in')
 else:
     print('password is not matched')
 
else:
     print('you are not a valid user')
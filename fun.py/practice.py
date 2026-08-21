'''teams = {
    "Brazil": [5, 2],
    "Argentina": [4, 3]
}

team = input("Enter team name: ")

if team in teams:
    wins = teams[team][0]
    losses = teams[team][1]

    percentage = wins / (wins + losses) * 100

    print("Winning percentage:", percentage, "%")
else:
    print("Team not found.")'''
    
'''numbers = [
    [1, 2, 3, 2, 1],
    [4, 2, 5, 3, 2],
    [1, 5, 2, 4, 2],
    [3, 2, 1, 5, 2],
    [2, 4, 3, 2, 5]
] 
count = {}
for row in numbers:
    for num in row:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
print(count)

num_sorted = sorted(count.items(),key = lambda x:x[1], reverse=True)
print(num_sorted)'''

 '''d=[ 
   {'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for item in d:
    if item['phone'][-1] == '8':
        print(item['phone'])
    if item['email'] == '':
     print(item['name'])'''

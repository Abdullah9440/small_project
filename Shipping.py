#A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
#items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
#program that asks the user how many items they are buying and prints the total cost.
item = int(input('how many items do you want to buy?'))
total = 0

if item <= 10:
    print('it will cost 12 for each')
    total = item * 12
elif item <= 99:
    print('item will cost 10 for each')
    total = item * 10
else :
    print('it will cose 7 for each')
    total =  item * 7
print("the total is = " ,total)

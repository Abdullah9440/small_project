'''dick = 

# Product ঢোকানো 
while True:
    name = input('enter product name and dollar or write done : ')
    if name == "done":
        break
    dollar = float(input('enter your dollar price here: '))
    dick[name] = dollar

# Amount-এর নিচে product খোঁজা
while True:
    amount_input = input('enter amount in dollar (or done): ')
    if amount_input == "done":
        break
    amount = float(amount_input)   # string থেকে number-এ convert

    for product_name, price in dick.items():
        if price < amount:
            print(product_name, "-", price)
            break
    else:
        print("No product found under this amount.")'''
        
'''days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

for month in sorted(days_in_month, key = lambda m: days_in_month[m]):
     print(f'{month} {days_in_month[month]}')'''
     
    
    
#password checker

     

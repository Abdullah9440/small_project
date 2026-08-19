'''products = []
prices = []

for i in range(3):
    product = input("Enter product name: ")
    price = float(input("Enter price: "))

    products.append(product)
    prices.append(price)

print("\nProduct              Original Price    Discount    Final Price")
print("-" * 65)

for i in range(3):
    discount = prices[i] * 0.11
    final_price = prices[i] - discount

    print(f"{products[i]:<20} {prices[i]:>13.2f} {discount:>10.2f} {final_price:>13.2f}")'''
   
'''count = 0
for i in range(1,1001):
    if '3' in str(i):
        count +=1
print(count)'''

'''feet = float(input('enter your feet and inches'))
inches =round((feet - int(feet))* 12)
print(f'you {int(feet)} feet, {inches}inches')'''
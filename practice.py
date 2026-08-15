import random 
number = []
for i in range(20):
    number.append(random.randint(1,100))
print(number)

largest = number[0]
smallest = number[0]
for num in number:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(f'the largest number is : ',largest)
print(f'the smallest number is : ',smallest)       



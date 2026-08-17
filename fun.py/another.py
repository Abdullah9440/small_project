#remove danger words
#words = input('enter sentense').split()
#curse_words = ["darn", "dang", "freakin", "heck", "shoot"]
#for i in range(len(words)):
#    if words[i] in curse_words:
#       words[i] = '*' * len(words[i])
#print(words)

#palindrom check using list comprehension 
#palindrom = [num for num in range(100,1000) if str(num)== str(num)[::-1]]
#print(palindrom)

#zero_separation = [1] + [x for i in range (1,11) for x in [0]*i + [1]]
#print(zero_separation)

#L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
#gaps = [L[i+1] - L[i] for i in range(len(L)-1)]
#max_gaps = max(gaps)
#percentage = gaps.count(2)/len(gaps)*100
#print(gaps)
#print(max_gaps)
#print(percentage)

#Write a program that creates a 1010 list of random integers between 1 and 100. Then do the
#following:
#(a) Print the list.
#(b) Find the largest value in the third row.
#(c) Find the smallest value in the sixth column.

#import random
#L = [[random.randint(1,100) for j in range(10)] for i in range(10)]
#largest = max(L[2])
#smallest = min(L[i][5] for i in range(10))
#print(L)
#print(largest)
#print(smallest)

#checkerboard pattern for 1 and 2,1 has to be start from upper left corner
#L = []
#for i in range(8):
#    row = []
#    for j in range(8):
#        if (i + j)%2 == 0:
#            row.append(1)
#        else:
#            row.append(2)
#    L.append(row)
#print(L)

'''L = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

target = sum(L[0])
wrong = 0

# Check rows
for i in range(4):
    if sum(L[i]) != target:
        wrong += 1

# Check columns
for j in range(4):
    total = 0

    for i in range(4):
        total += L[i][j]

    if total != target:
        wrong += 1

# First diagonal
total = 0

for i in range(4):
    total += L[i][i]

if total != target:
    wrong += 1

# Second diagonal
total = 0

for i in range(4):
    total += L[i][3-i]

if total != target:
    wrong += 1

# Final result
if wrong == 0:
    print("Magic Square")
else:
    print("Not Magic Square")'''
    
    
   
'''import random

characters = ['@', '5', '#', 'A', '!', '0', 'b', '$', 'z',
              'N', 'x', '-', '+', ':', 'c', '%', '&', '*']
items = characters * 2
random.shuffle(items)
board = []
for i in range(6):
    row = items[i*6:(i+1)*6]
    board.append(row)
for row in board:
 print(row)'''
 
 
 
 
 
 
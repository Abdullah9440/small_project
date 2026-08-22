'''def rectangle (m,n):
    row = m * '*'
    return (row + '\n') *n;


print(rectangle(3,4))'''

'''def excitement (word):
    new_list = []
    for i in range(len(word)):
        new_list.append(word[i] + '!' ) 
    return new_list;
original = ['hello','nice']
print(original)
print(excitement(original))'''

'''def sum_num (num):
    total = 0
    while num> 0:
        total = total + num % 10
        num = num // 10
    return total;

def root(n):
    while n >= 9:
     n =  sum_num(n)
    return n;
print(root(12345))'''


'''def first_def(str1,str2):
    min_length = min(len(str1),len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            return i;
    return -1
print(first_def('jellow','helloow'))
print(first_def('hello','hello'))'''  

'''def count_fact (n):
    n = abs(n)
    list_factor = []
    for i in range(1,n+1) :
         if n % i ==0:
            list_factor.append(i)
    return list_factor;
print(count_fact(20))'''

'''def match_str (s1,s2):
    return sum(1 for s1,s2 in zip(s1,s2) if s1 == s2)
print(match_str('python','pytorch'))'''


'''def find_index(str):
    location = []
    for i in range(len(str)):
        if str[i] == 'a':
         location.append(i)
    return location
print(find_index('abdullah al mamun'))'''

'''def name(s):
    if list(s) == sorted(s):
     return True
    return False
print(name('abcd'))'''


'''def same(s1,s2):
    if len(s1) == len(s2):
        return True
    return False
print(same('hello','jllow'))'''


'''def is_prime(n):
    if n<2:
     raise ValueError
    for i in range(2,n):
        if n % i == 0:
         return False
    return True
print(is_prime(7))    

def primes(n=100):
    primes_list = []
    candidate = 2
    while len(primes_list) < n:
       if is_prime(candidate):
        primes_list.append(candidate)
       candidate = candidate  + 1
    return primes_list
print(primes(8))'''


def verbose(n):
    ones = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
def merge_b(list1, list2):
    result = []
    i, j = 0, 0

   

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result
print(merge_b([5],[1,2,3]))
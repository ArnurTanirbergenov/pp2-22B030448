import math
import time
mylist = [1,3,5]
product = math.prod(mylist)
print(product)
#task2
string = 'AAAdddAaDd'
def counter(x):
    up = 0
    low = 0
    for ch in x:
        if ch.isupper():
            up += 1
        elif ch.islower():
            low += 1
    return up, low
print(counter(string))
#task3
palindrome = 'madam'
notpalin = 'Arnur'
print(palindrome == '' .join(reversed(palindrome)))
print(notpalin == '' .join(reversed(notpalin)))
#task4
x = int(input("Введите число "))
t = int(input("Введите время "))
time.sleep(t / 1000)
sqrt = x ** (0.5)
print(f'Square root of {x} after {t} miliseconds is {sqrt}')
#task5
tuple1 = (True, True, False)
tuple2 = (True, True, True)
tuple3 = (False, False)
print(all(tuple1), all(tuple2), all(tuple3))
#dir task1
import os
path = os.getcwd()
listdir = os.listdir(path)
print(listdir)
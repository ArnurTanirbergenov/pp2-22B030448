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
print('DIR:')
for dir in listdir:
    if os.path.isdir(dir):
        print(dir, end=" ")
print("\nFILES: ")
for file in listdir:
    if os.path.isfile(file):
        print(file, end= " ")
#dirtask2
path = r'F:/pythonProject1'
tocheck = os.path.join(path, "raw.txt")
print('exist', os.access(tocheck, os.F_OK))
print('readeable', os.access(tocheck, os.R_OK))
print('writable', os.access(tocheck, os.W_OK))
print('executable', os.access(tocheck, os.X_OK))
#task3
path = os.getcwd()
if os.path.exists(path):
    print(os.path.split(path))
#task4
path = r'F:/pythonProject1/raw.txt'
with open(path, 'r', encoding='utf8') as f:
    line = len(f.readlines())
print(line)
#task5
l = ['Arnur','doing','lab']
path = r'F:/pythonProject1/raw.txt'
with open(path,'w',encoding='utf8') as f:
    for x in l:
        f.write('%s\n' %x)
r = open(path)
print(r.read())
#task6
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in alph:
    file_name = c+".txt"
    with open(file_name, "w") as f:
        pass
#task7
path = r'F:/pythonProject1/raw.txt'
with open(path, 'r', encoding='utf8') as orig:
    with open('new.txt','w') as replica:
        replica.write(orig.read())
#task8
path8 = os.path.join(path, 'new.txt')
l = [os.access(path8, os.F_OK), os.access(path8, os.R_OK), 
     os.access(path8, os.W_OK), os.access(path8, os.X_OK)]
if all(l):
    os.remove(path8)
else:
    print('YOU ARE NOT ALLOWED')
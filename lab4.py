import datetime
tday = datetime.date.today()
tdelta = datetime.timedelta(days = 5)
print(tday - tdelta)
#task2
tday = datetime.date.today()
tdelta = datetime.timedelta(days = 1)
trow = tday + tdelta
yday = tday - tdelta
print("Yesterday ", yday)
print("Today ", tday)
print("Tomorrow ", trow)
#task3
tday = datetime.datetime.today().replace(microsecond=0)
print(tday)
#task4
date1 = datetime.datetime(2023, 1, 1, 0, 0, 1).replace(microsecond=0)
tday = datetime.datetime.today().replace(microsecond=0)
diff_sec = tday - date1
print(diff_sec.total_seconds())
#Generator task1
n = int(input("Введите число "))
def square(number):
    for x in range (1, n + 1):
        yield(x * x)
for x in square(n):
    print(x) 
#for task2
n = int(input("Введите число "))
mylist = []
def even(number):
    for x in range (1, n + 1):
        if x % 2 == 0:
            yield (x)
for x in even(n):
    mylist.append(str(x))
print(",".join(mylist))
#task3
n = int(input("Введите число "))
def div(n):
    for x in range (n):
        if x % 3 == 0 and x % 4 == 0:
            yield(x)
for x in div(n):
    print(x)
#task4
a = int(input("Введите число "))
b = int(input("Введите число "))
def squares(a,b):
    for x in range (a, b):
        if x % 2 == 0:
            yield (x)
for x in squares(a, b):
    assert x % 2 == 0, "Not even"
    print(x)
#task5
n = int(input("Введите число "))
def all(n):
    while n >= 0:
        yield(n)
        n -= 1
for x in all(n):
    print(x)
#MATH task1
import math
print(15 * math.pi / 180)
#task2
h = 5
b1 = 5
b2 = 6
print((b1 + b2)*h / 2)
#task3
n = 4 
lenght = 25
area = int(n * (lenght ** 2) / 4 * (math.tan(math.pi / n)))
print(area)
#task4
height = 6
lenght = 5
area = height * lenght
print(area)
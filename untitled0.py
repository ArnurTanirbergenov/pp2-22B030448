def ounces(a):
    return a * 28.3495231
x = int(input("Введите число "))
print(ounces(x))

#2
def t(b):
    return (5/9) * (b - 32)
x = int(input("Введите число "))
print(t(x))

#3
def solve(numheads, numlegs):
    chicks = 0
    rabbits = 0
    if numlegs % 2 != 0 or numheads == 0:
        print("Error")
    else:
        rabbits = (numlegs - 2*numheads)/2
        chickens = numheads - rabbits
        print("Chickens: " , int(chickens))
        print("Rabbits " , int(rabbits))
numheads = 35
numlegs = 94
solve(numheads, numlegs)

#4 

s = input("Введите числа ")
mylist = s.split()
def prime(values):
    for num in values:
        flag = True
        x = int(num)
        for i in range(2, x):
            if x % i == 0:
                flag = False
        if flag == True:
            print(x)
prime(mylist)
#5
import itertools
s = input("Введите строчку ")
def per(s):
    perm = list(itertools.permutations(s))
    print(perm)
per(s)
#6
def rev(string):
    mylist = string.split()
    mylist.reverse()
    s2 = ""
    for x in mylist:
        s2 += x
        s2 += " "
    return s2
print(rev("We are ready"))
#7
def has_33(mylist):
    counter = 0
    for x in mylist:
        if x == 3:
            counter += 1
        if counter == 2:
            return True
        elif x != 3:
            counter = 0
    return False
print(has_33([3, 1, 3]))
#8
def has_007(mylist):
    string = ""
    for x in mylist:
        if x == 0:
            string += str(x)
        elif x == 7:
            string += str(x)
    if string == "007":
        return True
    return False
print(has_007([1,2,4,0,0,7,5]))
print(has_007([1,0,2,4,0,5,7]))
print(has_007([1,7,2,0,4,5,0]))
#9
def volume(x):
    a = 4 * 3.14 * x / 3
    return a
print(volume(int(5)))
#10
def unique(mylist):
    newlist = []
    for x in mylist:
        if x not in newlist:
            newlist.append(x)
    return newlist
print(unique([1,4,6,3,1,3,2,4]))
#11
def palin(string):
    for i in range(0, int(len(string) / 2)):
        if string[i] != string [len(string) - i - 1]:
            return False
    return True
print(palin("madam"))
#12 
def hist(mylist):
    for x in mylist:
        string = ""
        while x > 0:
            string += '*'
            x -= 1
        print(string)
hist([4,9, 7])
#13
import random
print("Hello! What is your name?")
string = input()
print("Well, " + string + " I am thinking of a number between 1 and 20.")
def rand():
    x = random.randint(1,20)
    n = 0
    counter = 0
    while n != x:
        n = int(input("Take a guess\n"))
        if n > x:
            print("Your guess is to high")
        if n < x:
            print("Your guess is too low.")
        counter += 1  
    print("Good job, KBTU! You guessed my number in " + str(counter) + " guesses!")
rand()
#14
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def score_55(mylist, string1):
    for x in mylist:
        if x["name"] == string1:
            if x["imdb"] > 5.5:
                return True
            else:
                return False
def score_55_movies(mylist):
    list1 = []
    for x in mylist:
        if x["imdb"] > 5.5:
            list1.append(x["name"])
    return list1
def category(mylist,string1):
    list1 = []
    for x in mylist:
        if x["category"] == string1:
            list1.append(x["name"])
    return list1
def aver(mylist):
    counter = 0
    sum = 0
    for x in mylist:
        sum += x["imdb"]
        counter += 1
    return sum / counter
def aver_cat(mylist, string1):
    counter = 0
    sum = 0
    for x in mylist:
        if x["category"] == string1:
            sum += x["imdb"]
            counter += 1
    return sum / counter
print(score_55(movies, "Usual Suspects"))
print(score_55_movies(movies))
print(category(movies, "Suspense"))
print(aver(movies))
print(aver_cat(movies,"Romance"))
#classes
class fortask1():
    def __init__(self):
        self.stringname = ""
    def getstring(self):
        self.stringname = input()
    def printstring(self):
        print(self.stringname.upper())
string = fortask1()
string.getstring()
string.printstring()
#classestask2
class shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self, number):
        shape.__init__(self)
        self.lenght = number
    def area(self):
        return self.lenght * self.lenght
letsgo = square(10)
print(letsgo.area())
class rectangle(shape):
    def __init__(self,first, second):
        shape.__init__(self)
        self.lenght = first
        self.width = second
    def area(self):
        return self.lenght * self.width
recarea = rectangle(5, 6)
print(recarea.area())
#classestask4
class pointclass():
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def show(self, x, y):
        return f'X position = {x}, Y position = {y}'
    def change(self, x2, y2):
        self.x = self.x + x2
        self.y = self.y + y2
        return f'X position = {self.x}, Y position = {self.y}'
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5
point1 = pointclass(5, 17)
point2 = pointclass(3, 13)
print(point1.show(5, 17))
print(point1.distance(point2))
point1.change(3, 2)
print(point1.distance(point2))
#classestask5 
class bank():
    def __init__(self, owner : str, balance : int):
        self.owner = owner
        self.balance = balance
    def deposit(self, money:int):
        self.balance += money
        return f'You have {self.balance} now'
    def withdraw(self, money):
        if money > self.balance:
            return "You are not allowed to take more than is avaiable"
        else :
            self.balance -= money
        return f'You have {self.balance} now'
myacc = bank('Arnur', 100000)
print(myacc.deposit(10000))
print(myacc.withdraw(90000))
print(myacc.deposit(20000))
print(myacc.withdraw(40000))
#task6
mylist = [5, 6, 7, 8, 9, 10, 11, 12, 13]
def isprime(number):
    for i in range (2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
print(list(filter(lambda x: isprime(x), mylist)))

def myfilter(callback, iterable):
    filter_iterable = []
    for elem in iterable:
        if callback(elem):
            filter_iterable.append(elem)
    return filter_iterable

i = 1
txt = "Right now i = {}"
while i < 10:
    if i == 5:
        print("Half")
    else:
        print(txt.format(i))
    i += 1
else:
    print("NOW I IS EQUAL TO TEN")
fruits = ['banana', 'cherry', 'apple', 'mango', 'watermelon']
for x in fruits:
    print(x)
for x in range(2,11, 2):
    print(x)
###################
mylist = ["First element with index = 0", True, "So list can store different types of data",
          333]
print(mylist)
print(mylist[1])
print(mylist[-1])
print(mylist[1:3])
if True in mylist:
    print("True is in list")
mylist[1] = False
print(mylist)
mylist[0:2] = ["Changed", "True but in string format"] 
print(mylist)
mylist[1:2] = ["lol", ', i can do this ']
print(mylist[1])
mylist[0:3] = ["hmm"]
print(mylist)
mylist.insert(1,5)
print(mylist)
print(len(mylist))
mylist.append("a new one")
print(mylist)
mylist.pop(0)
print(mylist)
#########################################TUPLE
#Unchangeable,ordered(can have same things), can containt different datatypes at the same time
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
mytuple = ("heh", 'hoh', 'ha','heh', 'haha',1, True, 5, False)
print(mytuple)
tuplewith1element = ('one',)#without ',' python won't recognize tuple
print(len(mytuple))
if 'heh' in mytuple:
    print("Wow it is here")
for x in mytuple:
    print(x)
print(mytuple[0:3])
#########################################SET
#Unordered, unchangeable, unindexed, Set items are unchangeable, but you can remove items and add new items.
#Sets are unordered, so you cannot be sure in which order the items will appear.
#A set can contain different data types
myset = {'wow','wooooow', 'heh', 'sheesh','wow', 1, 5, True, 10}
print(myset)
print(len(myset))
for x in myset:
    print(x)
if 'wow' in myset:
    print("Wow is here")
print("wow" in myset)
myset.add(10000)
print(myset)
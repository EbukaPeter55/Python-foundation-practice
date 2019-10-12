thislist = ["apple", "banana", "cherry"]
print(thislist)

#Accessing list
print(thislist[1])

#change a list item
thislist[1] = "black currant"
print(thislist)

#loop through the list item
thislisting = ["apple", "onions", "tomatoe" ]
for x in thislisting:
    print(x)

#check if an element exists in an array
if "apple" in thislisting:
    print("Yes, 'apple' is in the fruit list")

#Print the number of items in a list
print(len(thislist))

#add item to the end of the list
thislisting.append("orange")
print(thislisting)

#add item at a specified index
thislist.insert(1, "stew")
print(thislist)

#Remove item from a list
thisitemize = ["apple", "strawberry", "icecream"]
thisitemize.remove("apple")
print(thisitemize)

#pop() removes the last item from a list
thisitemize.pop()
print(thisitemize)

#del keyword removes an item on a specified index
thisitemizing = ["strawberry", "onions", "chilli", "carrot"]
del thisitemizing[0]
print(thisitemizing)

#del keyword can also delete the list completely, and it gives an error
#del thisitemizing
#print(thisitemizing)

#The clear() method empties the list:
thisitemize.clear()
print(thisitemize)

#copy() is used to make a copy of a list
thiscontent = ["write", "study", "peruse"]
thisdetails = thiscontent.copy()
print(thisdetails)

#the list() method can also be used for copy

#the list() constructor can also be used in making a new list
thislista = list(("pepper", "banana", "cherry"))
print(thislista)


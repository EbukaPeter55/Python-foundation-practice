#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Accessing a tuple
print(thistuple[1])

#Looping through a tuple
thistuple = ("apple", "banana", "bread")
for x in thistuple:
  print(x)

#Check if an item exist
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#len() used to determine the length of a tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#You can not add or remove from a tuple, but can delete it complete using del()
# = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#You can use the tuple() constructor to produce new tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#The count() method returns the number of times a specified value appears in the tuple.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(7)
print(x)

#index() method finds the first occurrence of a value and return its postion
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)




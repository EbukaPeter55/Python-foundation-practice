#A dictionary is a collection which
#is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"]
print(x)

#You can also use the get() method to access
x = thisdict.get("model")
print(x)

#You can change the value of a specific item by referring to its key name:
#Change the "year" to 2018:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#You can loop through a dictionary by using a for loop. this returns the properties or key, there are methods to return the values
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

#You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)

#Loop through both keys and values, by using the items() function:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#To determine if a specified key is present in a dictionary use the in keyword:
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#To determine how many items (key-value pairs) a dictionary has, use the len() method.
print(len(thisdict))

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "blue"
print(thisdict)

#The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword can also delete the dictionary completely, and that would lead to an error:
#del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary

#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

#There are ways to make a copy, one way is to use the built-in Dictionary method copy().

#Example:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in method dict()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#It is also possible to use the dict() constructor to make a new dictionary:
thisdict =	dict(brand="Ford", model="Mustang", year=1934)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

#Python Dictionary fromkeys() Method
#The fromkeys() method returns a dictionary with the specified keys and values.
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value, see example below
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
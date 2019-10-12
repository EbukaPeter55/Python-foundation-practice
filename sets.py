#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thisset:
    print(x)

#check if an element is present in a set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#To add one item use add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#add multiple items with update() method
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#the len() method used to get the length of a set
print(len(thisset))

#"""To remove an item in a set, use the remove(), or the discard() method. both are same, except that 
#remove() throws an error when the element to be removed is absent, unlike discard() which does not.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#You can also use the pop(), method to remove an item, 
#but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)

#clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword deletes the set completely

#It is also possible to use the set() constructor to make a set.
setup = set(("apple", "banana", "berry"))
print(setup)

#python set difference method
#Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)

#difference_update() method remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

#python intersection() method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)

#intersection_update() #isdisjoint(), issubset(), issuperset(), symmetric_difference(), symmetric ifference update(), union()
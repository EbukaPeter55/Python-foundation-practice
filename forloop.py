#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#The for loop does not require an indexing variable to set beforehand.

fruits = ["apple", "mango", "orange"]
for x in fruits:
    print(x)

#Looping through a string
#Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)

#Break statement. With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

#Continue statement use to stop the current iteration of the loop and continue with the next.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Range function
#To loop through a set of code a specified number of times, we can use the range function
for x in range(7):
  print(x) 

#The range() function defaults to 0 as a starting value, 
#however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#Using the starter parameter
for x in range(2, 6):
  print(x) 

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nested loop. A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":
#This example Prints each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

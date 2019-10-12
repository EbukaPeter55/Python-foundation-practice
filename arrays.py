#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
#Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Accessing arrays
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)

#Modify the value of the first array
cars = ["Ford", "Volvo", "BMW"]

cars[1] = "Toyota"

print(cars)

#Use the len() method to return the length of an array (the number of elements in an array).
#Note: The length of an array is always one more than the highest array index.
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

#Looping array elements
#You can use the for in loop to loop through all the elements of an array.
for x in cars:
    print(x)

#You can use the append() method to add an element to an array.
cars.append("Honda")
print(cars)

#The pop() method is used to remove an element from the array..
cars.pop(1)
print(cars)

#You can also use the remove() method to remove an element from the array
cars = ["Ford", "Volvo", "BMW"]
cars.remove("BMW")
print(cars)
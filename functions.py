#A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#A function can return data as a result.
#In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")
my_function()

#Parameters are specified after the function name, inside the parentheses. 
#You can add as many parameters as you want, just separate them with a comma.
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Default parameter. If we call the function without parameter, it uses the default value:
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()

#You can send any data types of parameter to a function (string, number, list, dictionary etc.), 
#and it will be treated as the same data type inside the function.
#E.g. if you send a List as a parameter, it will still be a List when it reaches the function:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#To let a function return a value, use the return statement:
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


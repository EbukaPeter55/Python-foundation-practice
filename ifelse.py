#If statement. An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
    print("b is greater than a")

#Python relies on indentation, using whitespace, to define scope in the code. Other programming languages often use curly-brackets for this purpose.

#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
    print("a is greater than b")

#You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#If you have only one statement to execute, you can put it on the same line as the if statement using the shorthand if
if a > b: print("a is greater than b")

#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print ("B")

#Multiple else statement
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

#The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


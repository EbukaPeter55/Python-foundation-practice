a = "Hello, World!"
print(a[0])

#in python we can also get substrings
print(a[2:5])

#The strip() method removes any whitespace from the beginning or the end:
b = " Hello, man "
print(b.strip())

#The len() method returns the length of a string:
print(len(a))

#The lower() method returns the string in lower case:
print(a.lower())

#The upper() method returns the string in upper case:
c = "hello, world"
print(c.upper())

#The replace() method replaces a string with another string:
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
print(b.split(","))
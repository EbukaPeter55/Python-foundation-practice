#Python Iterators
#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:
#Return an iterator from a tuple, and print each value:
myturple = ("apple", "banana", "cherry")
myit = iter(myturple)

print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#We can also use a for loop to iterate through an iterable object:
myturple = ("apple", "banana", "cherry")

for x in myturple:
    print(x)

#Iterate the characters of a string, using a forloop:
mystr = "banana"
for x in mystr:
    print(x)

#To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object
#The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
#The __next__() method also allows you to do operations, and must return the next item in the sequence.
#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

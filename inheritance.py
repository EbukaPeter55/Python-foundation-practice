#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.
#Any class can be a parent class, syntax is same like creating any other class
#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()


#Create a child class
#Create a class named Student, which will inherit the properties and methods from the Person class or parent class:
class Student(Person):
    pass
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
#Now the Student class has the same properties and methods as the Person class.
x = Student("Mike", "Olsen")
x.printname()

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    Person.__init__(self, fname, lname)

x = Student("Ebuka", "Peter")
x.printname()

#Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
#Add a property called graduationyear to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    self.graduationyear = 2019
x = Student("John", "Peter")
print(x.graduationyear)

#In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. 
#To do so, add another parameter in the __init__() function:
#Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year
#creating the object 
x = Student("Ebuka", "Peter", "2019")
print(x.graduationyear)

#Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "John", 2019)
x.welcome()
#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
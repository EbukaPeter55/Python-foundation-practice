#The sort() method sorts the list aphabetically in ascending order by default
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

#You can use a function to sort the list with some criteria. reverse=true sorts it in descending order
cars = ['Fam', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)

# A function that returns the length of the value. key specifies the sorting criteria. so it will sort it by length in ascending order:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)

#sort() method
#Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

#Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

#Sort the list by the length of the values and reversed:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)
print(cars)
#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
#Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()

print(x)

#Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#Creating date object
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
#The datetime() class also takes parameters
#for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

#The strftime() Method
#The datetime object has a method for formatting date objects into readable strings.
#The method is called strftime(), and takes one parameter format, to specify the format of the returned string:
import datetime
x = datetime.datetime(2019, 7, 1)

print(x.strftime("%B"))
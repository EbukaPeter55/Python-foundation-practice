#JSON is a syntax for storing and exchanging data.
#Python has a built-in package called json, which can be used to work with JSON data.

#Parse JSON - Convert from JSON to Python
#If you have a JSON string, you can parse it by using the json.loads() method. The result will be a python dictionary
#import json
import json
#Some json:
x = '{ "name": "John", "age": "23", "city": "New York"}'
#Parse x
y = json.loads(x)
#the result is a python dictionary
print(y["age"])

#Convert python to json
#You can convert python objects(e.g list, turple, dictionaries. etc.) to json using the json.dumps() method.
import json
#A python object-(dictionary):
x = {
    "name": "John",
    "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


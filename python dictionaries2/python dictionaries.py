
#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#Dictionaries are written with curly brackets, and have keys and values:

#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "qwwerrrty",
  "model": "asd",
  "year": 15677
}
print(thisdict)

#Dictionary items are ordered, changeable, and does not allow duplicates.

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "qwwerrrty",
  "model": "asd",
  "year": 15677
}
print(thisdict["brand"])


#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

#Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

#Dictionaries cannot have two items with the same key:

#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

thisdict = {
  "brand": "qwwerrrty",
  "model": "asd",
  "year": 15677,
  "year": 22345
}
print(thisdict)

#To determine how many items a dictionary has, use the len() function:

#Print the number of items in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))

thisdict = {
  "brand": "qwwerrrty",
  "model": "asd",
  "year": 15677,
  "year": 22345
}
print(len(thisdict))

#The values in dictionary items can be of any data type:

#String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

my_dream_car = {
  "brand": "ECO.inc",
  "electric": True,
  "year": 2026,
  "colors": ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
}
print(my_dream_car)

#From Python's perspective, dictionaries are defined as objects with the data type 'dict':

#<class 'dict'>

#Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict = {
  "brand": "qwwerrrty",
  "model": "asd",
  "year": 15677,
  "year": 22345
}
print(type(thisdict))

#Dictionary is a collection which is ordered** and changeable. No duplicate members.

#When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

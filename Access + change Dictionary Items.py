
#You can access the items of a dictionary by referring to its key name, inside square brackets:

#Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

thisdict = {
  "brand": "",
  "model": "",
  "year": 0
}
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:

#Get the value of the "model" key:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

thisdict = {
  "brand": "",
  "model": "",
  "year": 0
}
x = thisdict.get("model")
print(x)

The keys() method will return a list of all the keys in the dictionary.

Example
Get a list of the keys:

thisdict = {
  "                       ": "Ford",
  "                     ": "Mustang",
  "                             ": 1964
}
x = thisdict.keys()
print(x)

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
x = E_shop.keys()
print(x) #before the change
E_shop["media"] = ["youtube", "redit"]
print(x) #after the change

#The values() method will return a list of all the values in the dictionary.

#Get a list of the values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
x = E_shop.values()
print(x)

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
x = E_shop.values()
print(x) #before the change
E_shop["food"] = "All-Food-Types"
print(x) #after the change

#Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "All-Food-Types"
}
x = E_shop.values()
print(x) #before the change
car["media"] = ["youtube", "redit"]
print(x) #after the change

#The items() method will return each item in a dictionary, as tuples in a list.

#Get a list of the key:value pairs

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "All-Food-Types"
}
x = E_shop.items()
print(x)

#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
x = E_shop.items()
print(x) #before the change
E_shop["food"] = "All-Food-Types"
print(x) #after the change

#Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "All-Food-Types"
}
x = E_shop.items()
print(x) #before the change
car["media"] = ["youtube", "redit"]
print(x) #after the change

#To determine if a specified key is present in a dictionary use the in keyword:

#Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "All-Food-Types"
}
if "food" in E_shop:
  print("Yes, 'food' is one of the keys in the E_shop dictionary")


#CHANGE DICTIONARY ITEMS

#You can change the value of a specific item by referring to its key name:

#Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
E_shop["food"] = "All-Food-Types"
print(E_shop)

#The update() method will update the dictionary with the items from the given argument.

#The argument must be a dictionary, or an iterable object with key:value pairs.

#Note:or an iterable object with key:value pairs.

#Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
E_shop.update({"food":"All-Food-Types"})
print(E_shop)

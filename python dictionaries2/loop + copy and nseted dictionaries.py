
#You can loop through a dictionary by using a for loop.

#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

#Print all key names in the dictionary, one by one:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

E_shop = {
  "clothes": "merch",
  "toys": "legos",
  "food": "sweets"
}
for x in E_shop:
  print(x)

#Print all values in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

E_shop = {
  "clothes": "merch",
  "toys": "legos",
  "food": "sweets"
}
for x in E_shop:
  print(E_shop[x])

#Print all values in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

E_shop = {
  "clothes": "merch",
  "toys": "legos",
  "food": "sweets"
}
for x in E_shop.values():
  print(x)

#You can use the keys() method to return the keys of a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

E_shop = {
  "clothes": "merch",
  "toys": "legos",
  "food": "sweets"
}
for x in E_shop.keys():
  print(x)

 #Loop through both keys and values, by using the items() method:

 thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

E_shop = {
  "clothes": "merch",
  "toys": "legos",
  "food": "sweets"
}
for x, y in E_shop.items():
  print(x, y)


#COPY DICTIONARYS

#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

#There are ways to make a copy, one way is to use the built-in Dictionary method copy().

#Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

E_shop = {
  "clothes": "merch",
  "toys": "legos",
  "food": "sweets"
}
inlegal_site = E_shop.copy()
print(inlegal_site)

#Another way to make a copy is to use the built-in function dict().

#Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

E_shop = {
  "clothes": "merch",
  "toys": "legos",
  "food": "sweets"
}
inlegal_site = dict(E_shop)
print(inlegal_site)


#NESTED DICTIONARYS

#A dictionary can contain dictionaries, this is called nested dictionaries.


#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

the_iloba_bros = {
  "child1" : {
    "name" : "Elijah",
    "year" : 2011
  },
  "child2" : {
    "name" : "Ezra",
    "year" : 2018
  },
  "child3" : {
    "name" : "Efran",
    "year" : 2021
  }
}
print(the_iloba_bros)

#Or, if you want to add three dictionaries into a new dictionary:

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}

child2 = {
  "name" : "Tobias",
  "year" : 2007
}

child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


"child1" = {
    "name" : "Elijah",
    "year" : 2011
  }

"child2" = {
    "name" : "Ezra",
    "year" : 2018
}

"child3" = {
    "name" : "Efran",
    "year" : 2021
  }

the_iloba_bros = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(the_iloba_bros)# all of mine dont work for nested dictionaries

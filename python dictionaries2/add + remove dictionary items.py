
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
E_shop["media"] = ["youtube", "redit"]
print(E_shop)

#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

#The argument must be a dictionary, or an iterable object with key:value pairs.

#Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
E_shop.update({"media" : ["youtube", "redit"]})
print(E_shop)


#REMOVE DICTIONARY ITEMS

#There are several methods to remove items from a dictionary:

#The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
E_shop.pop("food")
print(E_shop)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
E_shop.popitem()
print(E_shop)

#The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
del E_shop["clothes"]
print(E_shop)

#The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
del E_shop
print(E_shop)

#The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

E_shop = {
"clothes": "merch",
"toys": "legos",
"food": "sweets"
}
E_shop.clear()
print(E_shop)


#You cannot access items in a set by referring to an index or a key.

#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)




ADD ITEMS
--------------------------------------------------------------------------------
#Once a set is created, you cannot change its items, but you can add new items.

#To add one item to a set use the add() method.

#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {1, 2, 3}
thisset.add(4)
print(thisset)

#To add items from another set into the current set, use the update() method.

#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {1, 2, 3}
aliens = {"1", "2", "3"}
thisset.update(aliens)
print(thisset)

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {1 , 2, 3}
mylist = [4 ,5]
thisset.update(mylist)
print(thisset)

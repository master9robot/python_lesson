
#To remove an item in a set, use the remove(), or the discard() method.

#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {1, "2", 2}
thisset.remove("2")
print(thisset)

#Note: If the item to remove does not exist, remove() will raise an error.

#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {1, 2, 3}
thisset.discard("2")
print(thisset)

#Note: If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove the last item.

#Remember that sets are unordered, so you will not know what item that gets removed.

#The return value of the pop() method is the removed item.

#Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {1, 2, 3}
x = thisset.pop(2)
print(x)
print(thisset)

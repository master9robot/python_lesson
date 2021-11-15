
#You can access tuple items by referring to the index number, inside square brackets:

#Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = (1, 2, 3)
print(thistuple[2])

#Negative indexing means start from the end.

#-1 refers to the last item, -2 refers to the second last item etc.

#Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = (1, 2, 3)
print(thistuple[-2])

#You can specify a range of indexes by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new tuple with the specified items.

#Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = (1, 2, 3, 4, 5, 6, 7)
print(thistuple[2:5])

#By leaving out the start value, the range will start at the first item:

#This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = (1, 2, 3, 4, 5, 6, 7)
print(thistuple[:4])

#By leaving out the end value, the range will go on to the end of the list:

#This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = (1, 2, 3, 4, 5, 6, 7)
print(thistuple[2:])

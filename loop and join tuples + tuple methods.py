
#Loop Through a Tuple

#You can loop through the tuple items by using a for loop.

#Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = (1, 2, 3)
for x in thistuple:
  print(x)

#Loop Through the Index Numbers

#You can also loop through the tuple items by referring to their index number.

#Use the range() and len() functions to create a suitable iterable.

#Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = (1, 2, 3)
for i in range(len(thistuple)):
  print(thistuple[i])

#Using a While Loop

#You can loop through the list items by using a while loop.

#Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

#Remember to increase the index by 1 after each iteration.

#Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

thistuple = (1, 2, 3)
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#JOIN TUPLES

#To join two or more tuples you can use the + operator:

#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple1 = (1, 2, 3)
tuple2 = ("a1a", "a2a", "a3a")
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples

#If you want to multiply the content of a tuple a given number of times, you can use the * operator:

#Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

fruits = (1, 2, 3)
mytuple = fruits * 2
print(mytuple)


#TUPLE METHODS

#Python has two built-in methods that you can use on tuples.

Method	         Description
------------------------------------------------------------------------------------------------------------------------
count()	         Returns the number of times a specified value occurs in a tuple
index()	         Searches the tuple for a specified value and returns the position of where it was found
                                        Example


#ToList items are indexed and you can access them by referring to the index number:

#Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

list = ["one", "two", "three"]
print(list[-1])

#Negative indexing means start from the end

#-1 refers to the last item, -2 refers to the second last item etc.

#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["one", "two", "three"]
print(thislist[-2])

#You can specify a range of indexes by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new list with the specified items.

#Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

hislist = ["one", "two", "three", "four", "five", "six", "seven"]
print(thislist[3:6])

#By leaving out the start value, the range will start at the first item:

#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["one", "two", "three", "four", "five", "six", "seven"]
print(thislist[:4]) #
#By leaving out the end value, the range will go on to the end of the list:


#This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) "

thislist = ["one", "two", "three", "four", "five", "six", "seven"]
print(thislist[2:])

#Specify negative indexes if you want to start the search from the end of the list:

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["one", "two", "three", "four", "five", "six", "seven"]
print(thislist[-4:-1])

#To determine if a specified item is present in a list use the in keyword:

#Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
if "choclate" not in thislist:
  print("no, 'choclate' is not in the fruits list")


#To change the value of a specific item, refer to the index number:

#Change the second item:

this = ["apple", "banana", "cherry"]
this[1] = "blackcurrant"
print(this)# dosent work = should show "['apple', 'blackcurrant', 'cherry']"

this = [1, 2, 3]
this[1] = 2.0
print(this)# dosent work = should show "[1, 2.0, 3]"

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)# dosent work = should show "['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']"

thislist = [1, 2, 3, 4, 5, 6]
thislist[1:3] = [2.0, 2.5]
print(thislist)# dosent work = should show "[1, 2.0, 2.5, 3, 4, 5, 6]"

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist))# dosent work = should show "['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = [1, 2, 3]
thislist[1:2] = [2.25, 2.5]
print(thislist)# dosent work = should show "[1, 2.25, 2.5, 3]

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)# dosent work = should show "['apple', 'watermelon']"

thislist = [1, 2, 3]
thislist[1:3] = [1.5]
print(thislist)# dosent work = should show "[1, 1.5]"

#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

#The insert() method inserts an item at the specified index:

#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)# dosent work = should show "['apple', 'banana', 'watermelon', 'cherry']"

thislist = [1, 2, 3]
thislist.insert(2, 2.5)
print(thislist)# dosent work = should show "[1, 2, 2.5, 3]"

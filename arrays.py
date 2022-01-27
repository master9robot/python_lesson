
#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.


#Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

#Arrays are used to store multiple values in one single variable:

#Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]
print(cars)

foods = ["cake", "pasta", "sandwich"]
print(foods)

#An array is a special variable, which can hold more than one value at a time.

#If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
#However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

#The solution is an array!

#An array can hold many values under a single name, and you can access the values by referring to an index number.

#You refer to an array element by referring to the index number.

#Get the value of the first array item:

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

foods = ["cake", "pasta", "sandwich"]
x = foods[0]
print(x)

#Modify the value of the first array item:

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

foods = ["cake", "pasta", "sandwich"]
foods[0] = "cup cake"
print(foods)

#Use the len() method to return the length of an array (the number of elements in an array).

#Return the number of elements in the cars array:

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

foods = ["cake", "pasta", "sandwich"]
x = len(foods)
print(x)


#Note: The length of an array is always one more than the highest array index.

#You can use the for in loop to loop through all the elements of an array.

#Print each item in the cars array:

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

foods = ["cake", "pasta", "sandwich"]
for x in foods:
  print(x)

#You can use the append() method to add an element to an array.

#Add one more element to the cars array:

cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

foods = ["cake", "pasta", "sandwich"]
foods.append("hot dogs")
print(foods)

#You can use the pop() method to remove an element from the array.

#Delete the second element of the cars array:

cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

foods = ["cake", "pasta", "sandwich"]
foods.pop(1)
print(foods)

#You can also use the remove() method to remove an element from the array.

#Delete the element that has the value "Volvo":

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

foods = ["cake", "pasta", "sandwich"]
foods.remove("sandwich")
print(foods)

#Note: The list's remove() method only removes the first occurrence of the specified value.

#Python has a set of built-in methods that you can use on lists/arrays.

Method	    Description
-------------------------------------------------------------------------------------------------------------------------
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

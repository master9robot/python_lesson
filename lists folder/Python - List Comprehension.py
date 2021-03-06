
#List Comprehension

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

people_in_the_house = ["ELIJAH", "EZRA", "EFEREN", "UNKLE", "MUMMY"]
boys = []

for x in people_in_the_house:
  if "E" in x:
    boys.append(x)

print(boys)

#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


people_in_the_house = ["ELIJAH", "EZRA", "EFEREN", "UNKLE", "MUMMY"]

boys = [x for x in people_in_the_house if "E" in x]

print(boys)

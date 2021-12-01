
#You can loop through the set items by using a for loop:

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

  thisset = {1, 2, 3}
  for x in thisset:
    print(x)


#JOIN Sets

#There are several ways to join two or more sets in Python.

#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"", "", ""}
set2 = {}
set3 = set1.union(set2)
print(set3)

#Note: Both union() and update() will exclude any duplicate items.

#Keep ONLY the Duplicates

#The intersection_update() method will keep only the items that are present in both sets.

#Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

iloba_boys = {"elijah", "ezra", "eferan"}
kesterl_group = {"klea", "nataniel","elijah" }
iloba_boys.intersection_update(kesterl_group)
print(iloba_boys)

#The intersection() method will return a new set, that only contains the items that are present in both sets.

#Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

iloba_boys = {"elijah", "ezra", "eferan"}
kesterl_group = {"klea", "nataniel","elijah" }
E1 = iloba_boys.intersection(kesterl_group)
print(E1)

#Keep All, But NOT the Duplicates

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

#Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

tiny_iloba_boys = {"ezra", "eferan", "gy klea hates"}
kesterl_group = {"klea", "nataniel","elijah", "gy klea hates"}
tiny_iloba_boys.symmetric_difference_update(kesterl_group)
print(tiny_iloba_boys)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

#Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

tiny_iloba_boys = {"ezra", "eferan", "gy klea hates"}
kesterl_group = {"klea", "nataniel","elijah", "gy klea hates"}
people_i_like_as friends = tiny_iloba_boys.symmetric_difference(kesterl_group)
print(people_i_like_(as friends))#dosent work = should show "'eferan', 'nataniel', 'klea', 'elijah', 'ezra'}"

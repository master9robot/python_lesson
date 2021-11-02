
#To concatenate, or combine, two strings you can use the + operator.

#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)
a = "ptyon is"
b = " cool"
c = a + b
print(c)

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)
a = "ptyon is"
b = "cool"
c = a + " " + b
print(c)



STRING FORMATING

#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)
age = 36
txt2 = "My name is John, I am " + str(age)
print(txt2)

#But we can combine strings and numbers by using the format() method!

#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

#Use the format() method to insert numbers into strings:

age = 36
txt3 = "My name is John, and I am {}"
print(txt3.format(age))
age = 10
txt3 = "My name is eli, and I am {}"
print(txt3.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 'choclate bar'
price = 1000000.95
myorder = "I want {} pieces of {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 'choclate bar'
price = 1000000.95
myorder = "I want to pay {2} dollars for {0} pieces of {1}."
print(myorder.format(quantity, itemno, price))

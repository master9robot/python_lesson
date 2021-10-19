
#Strings in python are surrounded by either single quotation marks, or double quotation marks.

#'hello' is the same as "hello".

#You can display a string literal with the print() function:

print("Hello")
print('Hello')

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)


#You can assign a multiline string to a variable by using three quotes:

#You can use three double quotes:

b = """Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do eiusmod tempor ut labore et dolore magna aliqua."""
print(b)

#Or three single quotes:

c = '''Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do eiusmod tempor incididuntut labore et dolore magna aliqua.'''
print(c)

#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

#However, Python does not have a character data type, a single character is simply a string with a length of 1.

#Square brackets can be used to access elements of the string.


#Get the character at position 1 (remember that the first character has the position 0):

d = "Hello, World!"
print(d[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop.

#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#To get the length of a string, use the len() function.


#The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.

#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

#To check if a certain phrase or character is present in a string, we can use the keyword in.

#Check if "free" is present in the following text:

txt = "The best things in life are free!"#dosent work
if free in txt:#dosent work
    print("free!" in txt)#dosent work

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement:

#print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

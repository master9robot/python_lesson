
#Python has a set of built-in methods that you can use on strings.

#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
a = "asdfghjkl"
print(a.upper())

#The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())
a = "ASDFGHJKL"
print(a.lower())

#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = " asdfghjkl "
print(a.strip())

#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
a = "maya!"
print(a.replace("a", "o"))


#The split() method returns a list where the text between the specified separator becomes the list items.

#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
a = "qwerty, asdf"
print(a.split(",")) 

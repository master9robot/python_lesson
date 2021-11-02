
Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

METHOD              DESCRIPTION


--------------------------------------------------------------------------------------------------------------------------------------------
temooo  ='this is a rem'
hgfhggh = 'qwerty qwerty qwerty'
var2 = 't\th\ti\s is a r\te\tm'
temooo.capitalize()      # |Converts the first character to upper case
temooo.casefold()	      # |Converts string into lower case
temooo.center(101)	      #   |Returns a centered string
temooo.count('this is a rem')	  # |Returns the number of times a specified value occurs in a string
temooo.encode() #   | Returns an encoded version of the string
temooo.endswith('this is a rem i')
hgfhggh.endswith('qwerty')        # |Returns true if the string ends with the specified value
var2.expandtabs()	  #   |Sets the tab size of the string
temooo.find('h')   #   Searches the string for a specified value and returns the position of where it was found
temooo.format()
n = 'put the {} here and the {} there'
print(n.format('monkey ', 'fart')) #   |Formats specified values in a string
temooo.format_map()
a = {'x':'John', 'y':'Wick'}
print("{x}'s last name is {y}".format_map(a)) #   |Formats specified values in a string
temooo.index('h')	          # |searches the string for a specified value and returns the position of where it was found
temooo.isalnum()	      #   |Returns True if all characters in the string are alphanumeric
temooo.isalpha()	      #   |Returns True if all characters in the string are in the alphabet
temooo.isdecimal()	      # |Returns True if all characters in the string are decimals
temooo.isdigit()	      #   |Returns True if all characters in the string are digits
temooo.isidentifier()	  #  Returns True if the string is an identifier
temooo.islower()	      #Returns True if all characters in the string are lower case
temooo.isnumeric()	      # Returns True if all characters in the string are numeric
temooo.isprintable()	  #Returns True if all characters in the string are printable
temooo.isspace()	      #Returns True if all characters in the string are whitespaces
temooo.istitle()	      #Returns True if the string follows the rules of a title
temooo.isupper()	      #Returns True if all characters in the string are upper case
temooo.join('g')
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)  #   Joins the elements of an iterable to the end of the string
temooo.ljust()
txt = "lemons"
x = txt.ljust(20)
print(x, "are my favorite fruit.")#  Returns a left justified version of the string
temooo.lower()	          #  Converts a string into lower case
temooo.lstrip()
txt = "     lemons     "
txt.lstrip()
x = '     lemons     '
print("of all fruits", x, "are my favorite")#Returns a left trim version of the string
temooo.maketrans()
txt = "you love .ART!"
mytable = txt.maketrans(".", "F")
print(txt.translate(mytable))#Returns a translation table to be used in translations
temooo.partition()
txt = "I could eat lemons all day"
x = txt.partition("lemons")
print(x) #Returns a tuple where the string is parted into three parts
temooo.replace('r', 't')	      #Returns a string where a specified value is replaced with a specified value
temooo.rfind('rem')	           # Searches the string for a specified value and returns the last position of where it was found
temooo.rindex('rem')	         #Searches the string for a specified value and returns the last position of where it was found
temooo.rjust()
txt = "lemons"
x = txt.rjust(20)
print(x, "are my favorite fruit.")#Returns a right justified version of the string
temooo.rpartition()
  txt = "I could eat lemons all day, they are my favorite fruit"
x = txt.rpartition("lemons")
print(x)#	Returns a tuple where the string is parted into three parts
temooo.rsplit()
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)#Splits the string at the specified separator, and returns a list
temooo.rstrip()
x = '      lemons       '
print("of all fruits", x, "are my favorite")#Returns a right trim version of the string
temooo.split()
txt = "hi how are you"
x = txt.split()
print(x) #Splits the string at the specified separator, and returns a list
temooo.splitlines()
t = "do you like the music\we are in the jungle"
l = txt.splitlines()
print = (l)#Splits the string at line breaks and returns a list
temooo.startswith('this')       #Returns true if the string starts with the specified value
temooo.strip()	             #Returns a trimmed version of the string
temooo.swapcase()	        #Swaps cases, lower case becomes upper case and vice versa
temooo.title()  	        #Converts the first character of each word to upper case
temooo.translate()
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))#Returns a translated string.not done by self
temooo.upper() 	        #Converts a string into upper case
temooo.zfill()	            #Fills the string with a specified number of 0 values at the beginning
txt = "60"
x = txt.zfill(10)
print(x)

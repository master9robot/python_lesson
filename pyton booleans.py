
#Booleans represent one of two values: True or False.
#
#In programming you often need to know if an expression is True or False.

#You can evaluate any expression in Python, and get one of two answers, True or False.

#When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)
print(-10 < -11)
print(99 > 9)

#When you run a condition in an if statement, Python returns True or False:

#Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:#dosentwork
  print("b is not greater than a")

if 1 < 2:
     print("2 is greater than 1")
   else:#dosentwork
     print("2 is not greater than 1")

#The bool() function allows you to evaluate any value, and give you True or False in return,

#Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

print(bool("eli"))
print(bool(0))

#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

x2 = "eli-"
y2 = 0

print(bool(x2))
print(bool(y2))

#Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.

#The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool("xyz")
bool(789)
bool(["foot", "hand", "head"])

#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#You can create functions that returns a Boolean Value:

#Print the answer of a function:

def myFunction() :
  return True

print(myFunction())
#
Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :#not working
  return True#not working

if myFunction():#not working
  print("YES!")#not working
else:#not working
  print("NO!")#not working

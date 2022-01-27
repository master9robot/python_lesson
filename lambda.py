
#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

#lambda arguments : expression
#The expression is executed and the result is returned:

#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

e = lambda E : E + 134
print(e(9))

#Lambda functions can take any number of arguments:

#Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

e = lambda E, i : E * i
print(e(7, 9))

#Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

e = lambda E, i, I : E + i + I
print(e(3, 5, 7))

#Why Use Lambda Functions?

#The power of lambda is better shown when you use them as an anonymous function inside another function.

#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

#Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(e):
  return lambda E : E * e
mydoubler = myfunc(3)
print(mydoubler(85))

#Or, use the same function definition to make a function that always triples the number you send in:

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

def myfunc(e):
  return lambda E : E * e
mytripler = myfunc(3)
print(mytripler(85))

#Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

def myfunc(e):
  return lambda E : E * e
mydoubler = myfunc(4)
mytripler = myfunc(6)
print(mydoubler(0))
print(mytripler(0))

#Use lambda functions when an anonymous function is required for a short period of time.

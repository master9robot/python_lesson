#int
#float
#complex

x = 1    # int
print(type(x))
y = 2.8  # float
print(type(y))
z = 1j   # complex
print(type(z))

#Integers or int:

int1 = 1
int2 = 35656222554887711
int3 = -3255522

print(type(int1))
print(type(int2))
print(type(int3))

#Floats:

float1 = 1.10
float2 = 1.0
float3 = -35.59

print(type(float1))
print(type(float2))
print(type(float3))

Floats:

float4 = 35e3
e = 1e1
e
float5 = 12E4
float6 = -87.7e100
1.1e1
print(type(float4))
print(type(float5))
print(type(float6))

#Complex:

com1 = 3+5j
print(com1)
com2 = 5j
com3 = -5j

print(type(com1))
print(type(com2))
print(type(com3))

#Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Import the random module, and display a random number between 1 and 9:

import random
#test

print(random.randrange(1, 11))


#Integers:

x = int(1)   # x will be
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
float(4.2)

#Strings:

x = str("s1") # x will be 's1'
type(str('s1'))
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

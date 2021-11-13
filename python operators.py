
#Operators are used to perform operations on variables and values.

#In the example below, we use the + operator to add together two values:

print(10 + 5)

#Python divides the operators in the following groups:

#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operator
#Membership operators
#Bitwise operators


#PYTHON ARITHMETIC OPERATORS

#Arithmetic operators are used with numeric values to perform common mathematical operations:

x = 1
y = 2

Operator	Name	       Example
---------------------------------
+	      Addition         x + y
-	      Subtraction	   x - y
*	      Multiplication   x * y
/	      Division	       x / y
%	      Modulus	       x % y
**	      Exponentiation   x ** y
//	      Floor division   x // y


#PYTHON ASSIGNMENT OPERATORS

#Assignment operators are used to assign values to variables:

Operator	Example	  Same As
------------------------------------------------
=	        x = 5	  x = 5
+=	        x += 3	  x = x + 3
-=	        x -= 3	  x = x - 3
*=	        x *= 3	  x = x * 3
/=	        x /= 3	  x = x / 3
%=	        x %= 3	  x = x % 3
//=	        x //= 3	  x = x // 3
**=	        x **= 3	  x = x ** 3
&=	        x &= 3	  x = x & 3
|=	        x |= 3	  x = x | 3
^=	        x ^= 3	  x = x ^ 3
>>=	        x >>= 3	  x = x >> 3
<<=	        x <<= 3	  x = x << 3

#PYTHON COMPARISON OPERATORS

#Comparison operators are used to compare two values:

Operator	Name	                Example
------------------------------------------
==	       Equal	                x == y
!=	       Not equal	            x != y
>	       Greater than	            x > y
<	       Less than	            x < y
>=	       Greater than or equal to	x >= y
<=	       Less than or equal to	x <= y

#PYTHON LOJICAL OPERATORS

#Logical operators are used to combine conditional statements:

Operator	Name	                                                 Example
----------------------------------------------------------------------------------------------------------------------------------------------------------------
and 	    Returns True if both statements are true	             x < 5 and  x < 10
or	        Returns True if one of the statements is true	         x < 5 or x < 4
not	        Reverse the result, returns False if the result is true	 not(x < 5 and x < 10)

#PYTHON IDENTETY OPERATORS

#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

OperatoR  Description	                                        Example
-------------------------------------------------------------------------
is 	      Returns True if both variables are the same object	 x is y
is not	  Returns True if both variables are not the same objecT x is not y

#PYTHON MEMBERSHIP OPERATORS

#Membership operators are used to test if a sequence is presented in an object:

OperatoR Description	                                                                    Example
--------------------------------------------------------------------------------------------------------------------------------
in 	    Returns True if a sequence with the specified value is present in the object	    x in y
not in	Returns True if a sequence with the specified value is not present in the object	x not in y

#PYTHON BITWISE OPERATORS

#Bitwise operators are used to compare (binary) numbers:

Operator	Name	               Description
--------------------------------------------------------------------------------------------------------------------------------
& 	        AND	                   Sets each bit to 1 if both bits are 1
|	        OR	                   Sets each bit to 1 if one of two bits is 1
 ^	        XOR	                   Sets each bit to 1 if only one of two bits is 1
~ 	        NOT	                   Inverts all the bits
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed right shift	   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

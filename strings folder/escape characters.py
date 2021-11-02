
#To insert characters that are illegal in a string, use an escape character.

#An escape character is a backslash \ followed by the character you want to insert.

#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

#You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called "dragons" from the north."
#To fix this problem, use the escape character \":

#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
txt = "We are the so-called \"dragons\" from the north."
print(txt)

escape characters used in Python:

CODE             RESULT
 ------------------------
\'	      |      Single Quote
\\	      |      Backslash
\n	      |      New Line
\r	      |     Carriage Return
\t	      |      Tab
\b	      |      Backspace
\f	      |      Form Feed
\ooo      |      Octal value
\xhh	  |      Hex value

txt = "We are the so-called \'dragons\' from the north."
txt = "We are the so-called \\dragons\\ from the north."
txt = "We are the so-called \ndragons\n from the north."
txt = "We are the so-called \rdragons\r from the north."
txt = "We are the so-called \tdragons\t from the north."
txt = "We are the so-called \bdragons\b from the north."
txt = "We are the so-called \fdragons\f from the north."
txt = "We are the so-called \ooodragons\ooo from the north."#what should hapen
txt = "We are the so-called \xhhdragons\xhh from the north."#cased error

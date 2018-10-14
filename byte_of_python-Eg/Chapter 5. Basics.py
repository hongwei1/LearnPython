print('hello world') # Note that print is a function

# byte_of_python-Eg
#5.1 Comments
# Code tells you how, comments should tell you why.
# explain assumptions
# explain important decisions
# explain important details
# explain problems you're trying to solve
# explain problems you're trying to overcome in your program, etc.

#5.2 Literal Constants 
5
1.23
'This is a string'
"It's a string!"
# All these values can not be changed, they are just literal constants.

#5.3 Numbers : integers + floats.
2
3.23
5.23E-4 # E notation indicates powers of 10.


#5.3 Strings
# a sequences of charactoers. a bunch of words.
# 1 Single Quote
'Quote me on this'

#2 Double Quotes
"Quotes me on this" # the same as single 

#3 Triple Quotes
'''
This is a multi-line string. This is the first line.
This is the second line. 
"What's your name?," 
I asked. He said "Bond, James Bond." 
'''

""" 
This is a multi-line string. This is the first line.
This is the second line. 
"What's your name?," 
I asked. He said "Bond, James Bond." 
'''
"""

#4 Strings are Immutable
#5 The format method
# construct strings from other information.
age = 20 
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age)) 
print('Why is {0} playing with that python?'.format(name))

# using string concatenation.
# 1st: this is much unglier and error-prone. 
# 2rd: conversion to string would be done automatically. 
# 3rd: we can change the message without have to deal with the varibles used and vice-versa. 
name + 'is ' + str(age) + ' years old'


# the numbers are optional. 
print('{} was {} years old when he wrote this book'.format(name, age))

print('{0:.3f}'.format(1.0/3))

print ('{0:_^11}'.format('hello'))

print ('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))


print ("a"),print ("b"),

#5.4.6 Escape Sequences


s = '''This is a multi-line string. This is the second line.'''
print(s)
s =5
print(s)

s = '''This is a string.
    This does not continues the string.'''
s2 = 'This is a string' \
     'This continues the tring'





i = 5 # Error below! Notice a single space at the start of the line 
print ('Value is ')
# , i print 'I repeat, the value is ', i

































